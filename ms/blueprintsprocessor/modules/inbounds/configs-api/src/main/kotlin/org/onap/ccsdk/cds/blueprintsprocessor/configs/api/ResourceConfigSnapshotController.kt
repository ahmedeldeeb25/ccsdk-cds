/*
 * Copyright © 2019 Bell Canada
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

package org.onap.ccsdk.cds.blueprintsprocessor.configs.api

import com.fasterxml.jackson.databind.JsonNode
import io.swagger.annotations.Api
import io.swagger.annotations.ApiOperation
import io.swagger.annotations.ApiParam
import kotlinx.coroutines.runBlocking
import org.onap.ccsdk.cds.blueprintsprocessor.functions.config.snapshots.db.ResourceConfigSnapshot
import org.onap.ccsdk.cds.blueprintsprocessor.functions.config.snapshots.db.ResourceConfigSnapshotService
import org.onap.ccsdk.cds.controllerblueprints.core.asJsonPrimitive
import org.springframework.http.MediaType
import org.springframework.http.ResponseEntity
import org.springframework.security.access.prepost.PreAuthorize
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.ResponseBody
import org.springframework.web.bind.annotation.RestController

/**
 * Exposes Resource Configuration Snapshot API to store and retrieve stored resource configurations.
 *
 * @author Serge Simard
 * @version 1.0
 */
@RestController
@RequestMapping("/api/v1/configs")
@Api(
    value = "/api/v1/configs",
    description = "Interaction with stored configurations."
)
open class ResourceConfigSnapshotController(private val resourceConfigSnapshotService: ResourceConfigSnapshotService) {

    @RequestMapping(
        path = ["/health-check"],
        method = [RequestMethod.GET],
        produces = [MediaType.APPLICATION_JSON_VALUE]
    )
    @ResponseBody
    @ApiOperation(value = "Health Check", hidden = true)
    fun ressCfgSnapshotControllerHealthCheck(): JsonNode = runBlocking {
        "Success".asJsonPrimitive()
    }

    @RequestMapping(
        path = [""],
        method = [RequestMethod.GET],
        produces = [MediaType.TEXT_PLAIN_VALUE, MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE]
    )
    @ApiOperation(
        value = "Retrieve a resource configuration snapshot.",
        notes = "Retrieve a config snapshot, identified by its Resource Id and Type. " +
                "An extra 'format' parameter can be passed to tell what content-type is expected."
    )
    @ResponseBody
    @PreAuthorize("hasRole('USER')")
    fun get(
        @ApiParam(value = "Resource Type associated of the resource configuration snapshot.", required = false)
        @RequestParam(value = "resourceType", required = true) resourceType: String,

        @ApiParam(value = "Resource Id associated of the resource configuration snapshot.", required = false)
        @RequestParam(value = "resourceId", required = true) resourceId: String,

        @ApiParam(value = "Status of the snapshot being retrieved.", defaultValue = "RUNNING", required = false)
        @RequestParam(value = "status", required = false, defaultValue = "RUNNING") status: String,

        @ApiParam(
            value = "Expected format of the snapshot being retrieved.", defaultValue = MediaType.TEXT_PLAIN_VALUE,
            required = false
        )
        @RequestParam(value = "format", required = false, defaultValue = MediaType.TEXT_PLAIN_VALUE) format: String
    ):

            ResponseEntity<String> = runBlocking {

        var configSnapshot = ""

        if (resourceType.isNotEmpty() && resourceId.isNotEmpty()) {
            try {
                configSnapshot = resourceConfigSnapshotService.findByResourceIdAndResourceTypeAndStatus(
                    resourceId,
                    resourceType, ResourceConfigSnapshot.Status.valueOf(status.toUpperCase())
                )
            } catch (ex: NoSuchElementException) {
                throw ResourceConfigSnapshotException(
                    "Could not find configuration snapshot entry for type $resourceType and Id $resourceId"
                )
            }
        } else {
            throw IllegalArgumentException("Missing param. You must specify resource-id and resource-type.")
        }

        var expectedContentType = format
        if (expectedContentType.indexOf('/') < 0) {
            expectedContentType = "application/$expectedContentType"
        }
        val expectedMediaType: MediaType = MediaType.valueOf(expectedContentType)

        ResponseEntity.ok().contentType(expectedMediaType).body(configSnapshot)
    }

    @PostMapping(
        "/{resourceType}/{resourceId}/{status}",
        produces = [MediaType.APPLICATION_JSON_VALUE]
    )
    @ApiOperation(
        value = "Store a resource configuration snapshot identified by resourceId, resourceType, status.",
        notes = "Store a resource configuration snapshot, identified by its resourceId and resourceType, " +
                "and optionally its status, either RUNNING or CANDIDATE.",
        response = ResourceConfigSnapshot::class, produces = MediaType.APPLICATION_JSON_VALUE
    )
    @ResponseBody
    @PreAuthorize("hasRole('USER')")
    fun postWithResourceIdAndResourceType(
        @ApiParam(value = "Resource Type associated with the resolution.", required = false)
        @PathVariable(value = "resourceType", required = true) resourceType: String,
        @ApiParam(value = "Resource Id associated with the resolution.", required = false)
        @PathVariable(value = "resourceId", required = true) resourceId: String,
        @ApiParam(value = "Status of the snapshot being retrieved.", defaultValue = "RUNNING", required = true)
        @PathVariable(value = "status", required = true) status: String,
        @ApiParam(value = "Config snapshot to store.", required = true)
        @RequestBody snapshot: String
    ): ResponseEntity<ResourceConfigSnapshot> = runBlocking {

        val resultStored =
            resourceConfigSnapshotService.write(
                snapshot, resourceId, resourceType,
                ResourceConfigSnapshot.Status.valueOf(status.toUpperCase())
            )

        ResponseEntity.ok().body(resultStored)
    }
}
