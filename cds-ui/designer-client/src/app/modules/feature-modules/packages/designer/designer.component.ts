/*
============LICENSE_START==========================================
===================================================================
Copyright (C) 2019 Orange. All rights reserved.
===================================================================

Unless otherwise specified, all software contained herein is licensed
under the Apache License, Version 2.0 (the License);
you may not use this software except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
============LICENSE_END============================================
*/

import dagre from 'dagre';
import graphlib from 'graphlib';
import { Component, OnInit, ViewEncapsulation, OnDestroy } from '@angular/core';
import * as joint from 'jointjs';
import './jointjs/elements/palette.function.element';
import './jointjs/elements/action.element';
import './jointjs/elements/board.function.element';
import { DesignerStore } from './designer.store';
import { ActionElementTypeName } from 'src/app/common/constants/app-constants';
import { GraphUtil } from './graph.util';
import { GraphGenerator } from './graph.generator.util';
import { FunctionsStore } from './functions.store';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { distinctUntilChanged } from 'rxjs/operators';


@Component({
  selector: 'app-designer',
  templateUrl: './designer.component.html',
  styleUrls: ['./designer.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class DesignerComponent implements OnInit, OnDestroy {

  private controllerSideBar: boolean;
  private attributesSideBar: boolean;

  boardGraph: joint.dia.Graph;
  boardPaper: joint.dia.Paper;

  paletteGraph: joint.dia.Graph;
  palettePaper: joint.dia.Paper;
  private ngUnsubscribe = new Subject();
  private opt = { tx: 100, ty: 100 };

  constructor(private designerStore: DesignerStore,
              private functionStore: FunctionsStore,
              private graphUtil: GraphUtil,
              private graphGenerator: GraphGenerator) {
    this.controllerSideBar = true;
    this.attributesSideBar = false;

  }
  private _toggleSidebar1() {
    this.controllerSideBar = !this.controllerSideBar;
  }
  private _toggleSidebar2() {
    this.attributesSideBar = !this.attributesSideBar;
  }


  /**
   * - There is a board (main paper) that will the action and function selected from the palette
   * itmes in this board will be used to create tosca workflow and node templates
   * - There is also palette , whis contains all the possible functions and actions
   * that can be dragged into the board
   * - There is also a fly paper , which is temporarliy paper created on the fly
   * when items is dragged from the palette- and it's deleted when the item is dropped over
   * the board.
   * for more info about the drag and drop algorithem used please visit the following link:
   * https://stackoverflow.com/a/36932973/1340034
   */

  ngOnInit() {
    this.initializeBoard();
    this.initializePalette();
    this.stencilPaperEventListeners();

    /**
     * the code to retrieve from server is commented
     */
    this.functionStore.state$
      .pipe(
        distinctUntilChanged((a: any, b: any) => JSON.stringify(a) === JSON.stringify(b)),
        takeUntil(this.ngUnsubscribe))
      .subscribe(state => {

        if (state.serverFunctions) {
          console.log('inside subscriotn on functions store -->', state.serverFunctions);
          console.log(state);
          // this.viewedFunctions = state.functions;
          const list = state.serverFunctions;

          const cells = this.graphUtil.buildPaletteGraphFromList(list);
          this.paletteGraph.resetCells(cells);

          let idx = 0;
          cells.forEach(cell => {
            cell.translate(5, (cell.attributes.size.height + 5) * idx++);
          });
        }
      });

    this.designerStore.state$
      .pipe(
        distinctUntilChanged((a: any, b: any) => JSON.stringify(a) === JSON.stringify(b)),
        takeUntil(this.ngUnsubscribe))
      .subscribe(state => {
        if (state.sourceContent) {
          console.log('inside desinger.component---> ', state);
          // generate graph from store objects if exist
          const topologtTemplate = JSON.parse(state.sourceContent);
          console.log(topologtTemplate);
          delete state.sourceContent;
          this.graphGenerator.populate(topologtTemplate, this.boardGraph);

          console.log('all cells', this.boardGraph.getCells());
          /**
           * auto arrange elements in graph
           * https://resources.jointjs.com/docs/jointjs/v3.1/joint.html#layout.DirectedGraph
           */
          joint.layout.DirectedGraph.layout( this.boardGraph.getCells(), {
            dagre,
            graphlib,
            setLinkVertices: false,
            marginX: 10,
            marginY: 10,
            clusterPadding: { top: 100, left: 30, right: 10, bottom: 100 },
            rankDir: 'TB'
          });
        }
      });

    // action triggering
    this.functionStore.retrieveFuntions();

  }

  initializePalette() {
    if (!this.paletteGraph) {
      this.paletteGraph = new joint.dia.Graph();
      this.palettePaper = new joint.dia.Paper({
        el: $('#palette-paper'),
        model: this.paletteGraph,
        width: 300,
        height: $('#palette-paper').height(),
        // background: {
        //   color: 'rgba(0, 255, 0, 0.3)'
        // },
        interactive: false
        // elements in paletter need to be fixed, please refer to flying paper concept
      });
    }
  }

  initializeBoard() {
    if (!this.boardGraph) {
      console.log('initializeBoard...');
      this.boardGraph = new joint.dia.Graph();
      this.boardPaper = new joint.dia.Paper({
          el: $('#board-paper'),
          model: this.boardGraph,
          height: 720,
          width: 1100,
          gridSize: 10,
          drawGrid: true,
          // background: {
          //   color: 'rgba(0, 255, 0, 0.3)'
          // },
          cellViewNamespace: joint.shapes
        });

      this.boardPaper.on('all', element => {
        // console.log(element);
      });

      this.boardPaper.on('link:pointerdown', link => {
        console.log(link);
      });

      this.boardPaper.on('element:pointerdown', element => {
        // this.modelSelected.emit(element.model.get('model'));
      });

      this.boardPaper.on('blank:pointerclick', () => {
        // this.selectedModel = undefined;
      });

      this.boardGraph.on('change:position', (cell) => {

        const parentId = cell.get('parent');
        if (!parentId) {
          // this is action
          return;
        }

        const parent = this.boardGraph.getCell(parentId);

        const parentBbox = parent.getBBox();
        const cellBbox = cell.getBBox();
        if (parentBbox.containsPoint(cellBbox.origin()) &&
          parentBbox.containsPoint(cellBbox.topRight()) &&
          parentBbox.containsPoint(cellBbox.corner()) &&
          parentBbox.containsPoint(cellBbox.bottomLeft())) {

          // All the four corners of the child are inside
          // the parent area.
          return;
        }

        // Revert the child position.
        cell.set('position', cell.previous('position'));
      });
    }
    console.log('done initializing Board...');
  }

  insertCustomActionIntoBoard() {
    console.log('saving action to store action workflow....');
    const actionName = this.graphUtil.generateNewActionName();
    this.graphUtil.createCustomActionWithName(actionName, this.boardGraph);
    this.designerStore.addDeclarativeWorkFlow(actionName);
  }

  stencilPaperEventListeners() {
    this.palettePaper.on('cell:pointerdown', (draggedCell, pointerDownEvent, x, y) => {

      $('body').append(`
        <div id="flyPaper"
            style="position:fixed;z-index:100;opacity:.7;pointer-event:none;background-color: transparent !important;"></div>`
        );
      const flyGraph = new joint.dia.Graph();
      const flyPaper = new joint.dia.Paper({
          el: $('#flyPaper'),
          model: flyGraph,
          interactive: true
        });
      const flyShape = draggedCell.model.clone();
      const pos = draggedCell.model.position();
      const offset = {
        x: x - pos.x,
        y: y - pos.y
      };

      flyShape.position(0, 0);
      flyGraph.addCell(flyShape);
      $('#flyPaper').offset({
        left: pointerDownEvent.pageX - offset.x,
        top: pointerDownEvent.pageY - offset.y
      });
      $('body').on('mousemove.fly', mouseMoveEvent => {
        $('#flyPaper').offset({
          left: mouseMoveEvent.pageX - offset.x,
          top: mouseMoveEvent.pageY - offset.y
        });
      });

      $('body').on('mouseup.fly', mouseupEvent => {
        const mouseupX = mouseupEvent.pageX;
        const mouseupY = mouseupEvent.pageY;
        const target = this.boardPaper.$el.offset();
        // Dropped over paper ?
        if (mouseupX > target.left &&
          mouseupX < target.left + this.boardPaper.$el.width() &&
          mouseupY > target.top && y < target.top + this.boardPaper.$el.height()) {
          const functionType = this.graphUtil.getFunctionTypeFromPaletteFunction(flyShape);
          // step name is CDS realted terminology, please refer to tosca types
          const stepName = functionType;
          const functionElementForBoard = this.graphUtil.dropFunctionOverActionWithPosition(
              stepName, functionType,
              mouseupX, mouseupY,
              target, offset,
              this.boardGraph);

          const parentCell = this.graphUtil.getParent(functionElementForBoard, this.boardPaper);

          if (parentCell &&
              parentCell.model.attributes.type === ActionElementTypeName &&
            this.graphUtil.canEmpedMoreChildern(parentCell.model, this.boardGraph)) {

            if (this.graphUtil.isEmptyParent(parentCell.model)) {
              // first function in action
              const actionName = parentCell.model.attributes.attrs['#label'].text;
              this.designerStore.addStepToDeclarativeWorkFlow(actionName, stepName, functionType);
              if (functionType === 'dg-generic') {
                this.designerStore.addDgGenericNodeTemplate(stepName);
              } else {
                this.designerStore.addNodeTemplate(stepName, functionType);
              }
            } else {
              // second action means there was a dg-generic node before
              this.designerStore.addNodeTemplate(stepName, functionType);
              // this will fail if multiple dg-generic were added
              // TODO prevent multi functions of the same type inside the same action
              const dgGenericNode = this.graphUtil.getDgGenericChild(parentCell.model, this.boardGraph)[0];
              const dgGenericNodeName = this.graphUtil.getFunctionNameFromBoardFunction(dgGenericNode);
              this.designerStore.addDgGenericDependency(dgGenericNodeName, stepName);
            }


            // Prevent recursive embedding.
            if (parentCell &&
              parentCell.model.get('parent') !== functionElementForBoard.id) {
              parentCell.model.embed(functionElementForBoard);
            }
          } else {
            console.log('function dropped outside action or not allowed, rolling back...');
            alert('function dropped outside action or not allowed, rolling back...');
            functionElementForBoard.remove();
          }
        }
        $('body').off('mousemove.fly').off('mouseup.fly');
        // flyShape.remove();
        $('#flyPaper').remove();
      });
    });
    console.log('done stencilPaperEventListeners()...');
  }

  ngOnDestroy() {
    this.ngUnsubscribe.next();
    this.ngUnsubscribe.complete();
  }
}
