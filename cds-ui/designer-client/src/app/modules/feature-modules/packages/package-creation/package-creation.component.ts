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

import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {FilesContent, FolderNodeElement, MetaDataTabModel} from './mapping-models/metadata/MetaDataTab.model';

import * as JSZip from 'jszip';
import {PackageCreationStore} from './package-creation.store';
import {Definition} from './mapping-models/CBAPacakge.model';
import {PackageCreationModes} from './creationModes/PackageCreationModes';
import {PackageCreationBuilder} from './creationModes/PackageCreationBuilder';
import {PackageCreationUtils} from './package-creation.utils';
import {MetadataTabComponent} from './metadata-tab/metadata-tab.component';
import {Router} from '@angular/router';


@Component({
    selector: 'app-package-creation',
    templateUrl: './package-creation.component.html',
    styleUrls: ['./package-creation.component.css']
})
export class PackageCreationComponent implements OnInit {

    // adding initial referencing to designer mode


    constructor(private packageCreationStore: PackageCreationStore,
                private packageCreationUtils: PackageCreationUtils,
                private router: Router) {
    }

    counter = 0;
    modes: object[] = [
        {name: 'Designer Mode', style: 'mode-icon icon-designer-mode'},
        {name: 'Scripting Mode', style: 'mode-icon icon-scripting-mode'}];
    private metaDataTab: MetaDataTabModel = new MetaDataTabModel();
    private folder: FolderNodeElement = new FolderNodeElement();
    private zipFile: JSZip = new JSZip();
    private filesData: any = [];
    private definition: Definition = new Definition();

    @ViewChild(MetadataTabComponent, {static: false})
    private metadataTabComponent: MetadataTabComponent;

    @ViewChild('nameit', {static: true})
    private elementRef: ElementRef;

    ngOnInit() {
        this.elementRef.nativeElement.focus();
    }

    saveBluePrint() {
        this.packageCreationStore.state$.subscribe(
            cbaPackage => {
                console.log(cbaPackage);
                FilesContent.clear();
                let packageCreationModes: PackageCreationModes;
                cbaPackage = PackageCreationModes.mapModeType(cbaPackage);
                cbaPackage.metaData = PackageCreationModes.setEntryPoint(cbaPackage.metaData);
                packageCreationModes = PackageCreationBuilder.getCreationMode(cbaPackage);
                packageCreationModes.execute(cbaPackage, this.packageCreationUtils);
                this.filesData.push(this.folder.TREE_DATA);
                this.saveBluePrintToDataBase();
            });


    }


    saveBluePrintToDataBase() {
        this.create();
        this.zipFile.generateAsync({type: 'blob'})
            .then(blob => {
                this.packageCreationStore.saveBluePrint(blob);
                this.router.navigate(['/packages']);
            });
    }


    create() {
        FilesContent.getMapOfFilesNamesAndContent().forEach((value, key) => {
            this.zipFile.folder(key.split('/')[0]);
            this.zipFile.file(key, value);
        });

    }

    test() {
        this.metadataTabComponent.saveMetaDataToStore();
    }

    goBackToDashBorad() {
        this.router.navigate(['/packages']);
    }
}
