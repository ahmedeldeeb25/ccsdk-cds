/*
 *  Copyright © 2017-2018 AT&T Intellectual Property.
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

package org.onap.ccsdk.apps.controllerblueprints.resource.dict.service

import com.att.eelf.configuration.EELFLogger
import org.junit.Assert
import org.junit.Test
import org.onap.ccsdk.apps.controllerblueprints.core.BluePrintException
import org.onap.ccsdk.apps.controllerblueprints.core.utils.JacksonUtils
import org.onap.ccsdk.apps.controllerblueprints.resource.dict.ResourceAssignment
import com.att.eelf.configuration.EELFManager
/**
 * ResourceAssignmentValidationServiceTest.
 *
 * @author Brinda Santh
 */
class ResourceAssignmentValidationServiceTest {
    private val log: EELFLogger = EELFManager.getInstance().getLogger(ResourceAssignmentValidationServiceTest::class.java)
    @Test
    fun testValidateSuccess() {
        log.info("**************** testValidateSuccess *****************")
        val assignments = JacksonUtils.getListFromClassPathFile("validation/success.json", ResourceAssignment::class.java)
        val resourceAssignmentValidator = ResourceAssignmentValidationDefaultService()
        val result = resourceAssignmentValidator.validate(assignments!!)
        Assert.assertTrue("Failed to Validate", result)
    }

    @Test(expected = BluePrintException::class)
    fun testValidateDuplicate() {
        log.info(" **************** testValidateDuplicate *****************")
        val assignments = JacksonUtils.getListFromClassPathFile("validation/duplicate.json", ResourceAssignment::class.java)
        val resourceAssignmentValidator = ResourceAssignmentValidationDefaultService()
        resourceAssignmentValidator.validate(assignments!!)
    }

    @Test(expected = BluePrintException::class)
    fun testValidateCyclic() {
        log.info(" ****************  testValidateCyclic *****************")
        val assignments = JacksonUtils.getListFromClassPathFile("validation/cyclic.json", ResourceAssignment::class.java)
        val resourceAssignmentValidator = ResourceAssignmentValidationDefaultService()
        resourceAssignmentValidator.validate(assignments!!)
    }
}