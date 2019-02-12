/*
 *  Copyright © 2018 IBM.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package org.onap.ccsdk.apps.blueprintsprocessor.functions.restconf.executor

import org.onap.ccsdk.apps.blueprintsprocessor.rest.service.BluePrintRestLibPropertyService
import org.onap.ccsdk.apps.blueprintsprocessor.rest.service.BlueprintWebClientService
import org.onap.ccsdk.apps.blueprintsprocessor.services.execution.AbstractComponentFunction


abstract class RestconfComponentFunction : AbstractComponentFunction() {

    lateinit var bluePrintRestLibPropertyService: BluePrintRestLibPropertyService

    fun restClientService(selector: String): BlueprintWebClientService {
        return bluePrintRestLibPropertyService.blueprintWebClientService(selector)
    }


}