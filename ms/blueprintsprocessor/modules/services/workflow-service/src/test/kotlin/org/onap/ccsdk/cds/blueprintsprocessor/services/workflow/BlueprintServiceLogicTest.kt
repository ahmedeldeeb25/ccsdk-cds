/*
 * Copyright © 2017-2018 AT&T Intellectual Property.
 * Modifications Copyright © 2019 IBM.
 *
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
 */

package org.onap.ccsdk.cds.blueprintsprocessor.services.workflow

import kotlinx.coroutines.runBlocking
import org.junit.Test
import org.junit.runner.RunWith
import org.onap.ccsdk.cds.blueprintsprocessor.core.api.data.ExecutionServiceInput
import org.onap.ccsdk.cds.blueprintsprocessor.services.workflow.executor.ComponentExecuteNodeExecutor
import org.onap.ccsdk.cds.blueprintsprocessor.services.workflow.mock.PrototypeComponentFunction
import org.onap.ccsdk.cds.blueprintsprocessor.services.workflow.mock.SingletonComponentFunction
import org.onap.ccsdk.cds.controllerblueprints.core.utils.BluePrintMetadataUtils
import org.onap.ccsdk.cds.controllerblueprints.core.utils.JacksonUtils
import org.slf4j.LoggerFactory
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.context.ApplicationContext
import org.springframework.test.context.ContextConfiguration
import org.springframework.test.context.junit4.SpringRunner
import kotlin.test.assertEquals

@RunWith(SpringRunner::class)
@ContextConfiguration(classes = [WorkflowServiceConfiguration::class, ComponentExecuteNodeExecutor::class])
class BlueprintServiceLogicTest {

    private val log = LoggerFactory.getLogger(BlueprintServiceLogicTest::class.java)

    @Autowired
    lateinit var applicationContext: ApplicationContext

    @Autowired
    lateinit var dgWorkflowExecutionService: DGWorkflowExecutionService

    @Test
    fun testExecuteGraphWithSingleComponent() {

        val bluePrintRuntimeService = BluePrintMetadataUtils.getBluePrintRuntime("1234",
                "./../../../../../components/model-catalog/blueprint-model/test-blueprint/baseconfiguration")

        val executionServiceInput = JacksonUtils.readValueFromClassPathFile("execution-input/resource-assignment-input.json", ExecutionServiceInput::class.java)!!

        runBlocking {
            dgWorkflowExecutionService.executeBluePrintWorkflow(bluePrintRuntimeService, executionServiceInput, mutableMapOf())
        }


    }

    @Test
    fun testExecuteGraphWithMultipleComponents() {

        val bluePrintRuntimeService = BluePrintMetadataUtils.getBluePrintRuntime("1234",
                "./../../../../../components/model-catalog/blueprint-model/test-blueprint/baseconfiguration")

        val executionServiceInput = JacksonUtils.readValueFromClassPathFile("execution-input/assign-activate-input.json", ExecutionServiceInput::class.java)!!

        runBlocking {
            dgWorkflowExecutionService.executeBluePrintWorkflow(bluePrintRuntimeService, executionServiceInput, mutableMapOf())
        }

    }

    @Test
    fun testSingleton() {
        val singleton1 = applicationContext.getBean(SingletonComponentFunction::class.java)
        singleton1.stepName = "step1"
        val singleton2 = applicationContext.getBean(SingletonComponentFunction::class.java)
        assertEquals(singleton1.stepName, singleton2.stepName, " failed to get singleton data")
    }

    @Test
    fun testProtoTypeFunction() {
        val stepName1 = "step1"
        val stepName2 = "step2"
        val proto1 = applicationContext.getBean(PrototypeComponentFunction::class.java)
        proto1.stepName = stepName1

        val proto2 = applicationContext.getBean(PrototypeComponentFunction::class.java)
        proto2.stepName = stepName2

        assertEquals(stepName1, proto1.stepName, " Failed to match the step1 name")
        assertEquals(stepName2, proto2.stepName, " Failed to match the step2 name")
    }

}