/*
* ============LICENSE_START=======================================================
* ONAP : CDS
* ================================================================================
* Copyright 2019 TechMahindra
*
* Modifications Copyright (C) 2019 IBM
*=================================================================================
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
* ============LICENSE_END=========================================================
*/

import { Component, OnInit, EventEmitter, Output  } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { IResources } from 'src/app/common/core/store/models/resources.model';
import { IResourcesState } from 'src/app/common/core/store/models/resourcesState.model';
import { Observable, from } from 'rxjs';
import { Store } from '@ngrx/store';
import { IAppState } from '../../../../common/core/store/state/app.state';
import { A11yModule } from '@angular/cdk/a11y';

import { LoadResourcesSuccess } from 'src/app/common/core/store/actions/resources.action';
import { IPropertyData } from 'src/app/common/core/store/models/propertyData.model';
import { IEntrySchema } from 'src/app/common/core/store/models/entrySchema.model';
import { ResourceEditService } from '../resource-edit.service';

@Component({
  selector: 'app-resource-metadata',
  templateUrl: './resource-metadata.component.html',
  styleUrls: ['./resource-metadata.component.scss']
})
export class ResourceMetadataComponent implements OnInit {
    entry_schema:IEntrySchema;
    properties: any = {};
    ResourceMetadata: FormGroup;
    resource_name: string;
    tags: string;
    rdState: Observable<IResourcesState>;
    resources: IResources;
    propertyValues = [];
    property = [];   
    @Output() resourcesData = new EventEmitter();
    dataTypeList: any[] = [
       {modelName: 'String'}, {modelName: 'Boolean'}, {modelName: 'Integer'}, {modelName: 'Float'}, {modelName: 'Double'}
    ];
     
 constructor(private formBuilder: FormBuilder, 
             private store: Store<IAppState>, 
             private resourceEditService: ResourceEditService) { 
    this.rdState = this.store.select('resources');
    this.ResourceMetadata = this.formBuilder.group({
        Resource_Name: ['', Validators.required],
       _tags: ['', Validators.required],
       _description : ['', Validators.required],
       _type: ['', Validators.required],
       required: ['', Validators.required],
       entry_schema: ['']
    });   
 }

 ngOnInit() {
    this.resourceEditService.getDataTypes()
    .subscribe(data=>{
      console.log(data);
      if(data) {
         data.forEach(element => {
            this.dataTypeList.push(element);
         });
      }
    }, (error)=>{
       console.log("There is an error");
    });
    this.rdState.subscribe(
      resourcesdata => {
        var resourcesState: IResourcesState = { resources: resourcesdata.resources, isLoadSuccess: resourcesdata.isLoadSuccess, isSaveSuccess: resourcesdata.isSaveSuccess, isUpdateSuccess: resourcesdata.isUpdateSuccess };
        this.resource_name = resourcesState.resources.name;
        this.tags = resourcesState.resources.tags;
        this.resources = resourcesState.resources;
        if (resourcesState.resources.definition && resourcesState.resources.definition.property) {
         this.properties= resourcesState.resources.definition.property;
        } else {
           this.properties['description']= '';
           this.properties['type'] = '';
           this.properties['entry_schema'] = '';
           this.properties['required'] = false;
        }
      //   this.propertyValues=  this.checkNested(this.properties);
        this.ResourceMetadata = this.formBuilder.group({
        Resource_Name: [this.resource_name, Validators.required],
         _tags: [this.tags, Validators.required],
         _description : [ this.properties.description, Validators.required, ''],
         _type: [ this.properties.type, Validators.required],
         required: [ JSON.stringify(this.properties.required), Validators.required],
         entry_schema: [this.properties.entry_schema]
      });   
    })
 }
  
 UploadMetadata() {
  
    this.resources.name = this.ResourceMetadata.value.Resource_Name;
    this.resources.tags = this.ResourceMetadata.value._tags;
    this.resources.definition.property.description = this.ResourceMetadata.value._description;
    this.resources.definition.property.type = this.ResourceMetadata.value._type;
    this.resources.definition.property.required = this.ResourceMetadata.value.required;
    this.resources.definition.property.entry_schema = this.ResourceMetadata.value.entry_schema;
 	this.resourcesData.emit(this.resources); 
 }
   
 checkNested(obj) {
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      if (typeof obj[key] == "object"){
         console.log(`Key: ${key}`)
         this.checkNested(obj[key]);
      } else {
         this.property.push(obj[key]);             
      }   
     }
   }
   return this.property
 }
}