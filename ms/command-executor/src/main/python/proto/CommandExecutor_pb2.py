# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommandExecutor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CommandExecutor.proto',
  package='org.onap.ccsdk.cds.controllerblueprints.command.api',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x15\x43ommandExecutor.proto\x12\x33org.onap.ccsdk.cds.controllerblueprints.command.api\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8f\x02\n\x0e\x45xecutionInput\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x15\n\rcorrelationId\x18\x02 \x01(\t\x12U\n\x0bidentifiers\x18\x03 \x01(\x0b\x32@.org.onap.ccsdk.cds.controllerblueprints.command.api.Identifiers\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07timeOut\x18\x05 \x01(\x05\x12+\n\nproperties\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd0\x02\n\x0fPrepareEnvInput\x12U\n\x0bidentifiers\x18\x01 \x01(\x0b\x32@.org.onap.ccsdk.cds.controllerblueprints.command.api.Identifiers\x12\x11\n\trequestId\x18\x02 \x01(\t\x12\x15\n\rcorrelationId\x18\x03 \x01(\t\x12O\n\x08packages\x18\x04 \x03(\x0b\x32=.org.onap.ccsdk.cds.controllerblueprints.command.api.Packages\x12\x0f\n\x07timeOut\x18\x05 \x01(\x05\x12+\n\nproperties\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\">\n\x0bIdentifiers\x12\x15\n\rblueprintName\x18\x01 \x01(\t\x12\x18\n\x10\x62lueprintVersion\x18\x02 \x01(\t\"\xcb\x01\n\x0f\x45xecutionOutput\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x10\n\x08response\x18\x02 \x03(\t\x12S\n\x06status\x18\x03 \x01(\x0e\x32\x43.org.onap.ccsdk.cds.controllerblueprints.command.api.ResponseStatus\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07payload\x18\x05 \x01(\t\"k\n\x08Packages\x12N\n\x04type\x18\x01 \x01(\x0e\x32@.org.onap.ccsdk.cds.controllerblueprints.command.api.PackageType\x12\x0f\n\x07package\x18\x02 \x03(\t**\n\x0eResponseStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01*9\n\x0bPackageType\x12\x07\n\x03pip\x10\x00\x12\x12\n\x0e\x61nsible_galaxy\x10\x01\x12\r\n\tutilities\x10\x02\x32\xd1\x02\n\x16\x43ommandExecutorService\x12\x98\x01\n\nprepareEnv\x12\x44.org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput\x1a\x44.org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput\x12\x9b\x01\n\x0e\x65xecuteCommand\x12\x43.org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput\x1a\x44.org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutputB\x02P\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_RESPONSESTATUS = _descriptor.EnumDescriptor(
  name='ResponseStatus',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1133,
  serialized_end=1175,
)
_sym_db.RegisterEnumDescriptor(_RESPONSESTATUS)

ResponseStatus = enum_type_wrapper.EnumTypeWrapper(_RESPONSESTATUS)
_PACKAGETYPE = _descriptor.EnumDescriptor(
  name='PackageType',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PackageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='pip', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ansible_galaxy', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='utilities', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1177,
  serialized_end=1234,
)
_sym_db.RegisterEnumDescriptor(_PACKAGETYPE)

PackageType = enum_type_wrapper.EnumTypeWrapper(_PACKAGETYPE)
SUCCESS = 0
FAILURE = 1
pip = 0
ansible_galaxy = 1
utilities = 2



_EXECUTIONINPUT = _descriptor.Descriptor(
  name='ExecutionInput',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.requestId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='correlationId', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.correlationId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.identifiers', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.command', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeOut', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.timeOut', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.properties', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput.timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=413,
)


_PREPAREENVINPUT = _descriptor.Descriptor(
  name='PrepareEnvInput',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.identifiers', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestId', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.requestId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='correlationId', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.correlationId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packages', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.packages', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeOut', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.timeOut', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.properties', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput.timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=752,
)


_IDENTIFIERS = _descriptor.Descriptor(
  name='Identifiers',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.Identifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blueprintName', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.Identifiers.blueprintName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blueprintVersion', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.Identifiers.blueprintVersion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=754,
  serialized_end=816,
)


_EXECUTIONOUTPUT = _descriptor.Descriptor(
  name='ExecutionOutput',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput.requestId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput.response', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput.payload', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=1022,
)


_PACKAGES = _descriptor.Descriptor(
  name='Packages',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.Packages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.Packages.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package', full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.Packages.package', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1024,
  serialized_end=1131,
)

_EXECUTIONINPUT.fields_by_name['identifiers'].message_type = _IDENTIFIERS
_EXECUTIONINPUT.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EXECUTIONINPUT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PREPAREENVINPUT.fields_by_name['identifiers'].message_type = _IDENTIFIERS
_PREPAREENVINPUT.fields_by_name['packages'].message_type = _PACKAGES
_PREPAREENVINPUT.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_PREPAREENVINPUT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXECUTIONOUTPUT.fields_by_name['status'].enum_type = _RESPONSESTATUS
_EXECUTIONOUTPUT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PACKAGES.fields_by_name['type'].enum_type = _PACKAGETYPE
DESCRIPTOR.message_types_by_name['ExecutionInput'] = _EXECUTIONINPUT
DESCRIPTOR.message_types_by_name['PrepareEnvInput'] = _PREPAREENVINPUT
DESCRIPTOR.message_types_by_name['Identifiers'] = _IDENTIFIERS
DESCRIPTOR.message_types_by_name['ExecutionOutput'] = _EXECUTIONOUTPUT
DESCRIPTOR.message_types_by_name['Packages'] = _PACKAGES
DESCRIPTOR.enum_types_by_name['ResponseStatus'] = _RESPONSESTATUS
DESCRIPTOR.enum_types_by_name['PackageType'] = _PACKAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecutionInput = _reflection.GeneratedProtocolMessageType('ExecutionInput', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONINPUT,
  '__module__' : 'CommandExecutor_pb2'
  # @@protoc_insertion_point(class_scope:org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionInput)
  })
_sym_db.RegisterMessage(ExecutionInput)

PrepareEnvInput = _reflection.GeneratedProtocolMessageType('PrepareEnvInput', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREENVINPUT,
  '__module__' : 'CommandExecutor_pb2'
  # @@protoc_insertion_point(class_scope:org.onap.ccsdk.cds.controllerblueprints.command.api.PrepareEnvInput)
  })
_sym_db.RegisterMessage(PrepareEnvInput)

Identifiers = _reflection.GeneratedProtocolMessageType('Identifiers', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIERS,
  '__module__' : 'CommandExecutor_pb2'
  # @@protoc_insertion_point(class_scope:org.onap.ccsdk.cds.controllerblueprints.command.api.Identifiers)
  })
_sym_db.RegisterMessage(Identifiers)

ExecutionOutput = _reflection.GeneratedProtocolMessageType('ExecutionOutput', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONOUTPUT,
  '__module__' : 'CommandExecutor_pb2'
  # @@protoc_insertion_point(class_scope:org.onap.ccsdk.cds.controllerblueprints.command.api.ExecutionOutput)
  })
_sym_db.RegisterMessage(ExecutionOutput)

Packages = _reflection.GeneratedProtocolMessageType('Packages', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGES,
  '__module__' : 'CommandExecutor_pb2'
  # @@protoc_insertion_point(class_scope:org.onap.ccsdk.cds.controllerblueprints.command.api.Packages)
  })
_sym_db.RegisterMessage(Packages)


DESCRIPTOR._options = None

_COMMANDEXECUTORSERVICE = _descriptor.ServiceDescriptor(
  name='CommandExecutorService',
  full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.CommandExecutorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1237,
  serialized_end=1574,
  methods=[
  _descriptor.MethodDescriptor(
    name='prepareEnv',
    full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.CommandExecutorService.prepareEnv',
    index=0,
    containing_service=None,
    input_type=_PREPAREENVINPUT,
    output_type=_EXECUTIONOUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='executeCommand',
    full_name='org.onap.ccsdk.cds.controllerblueprints.command.api.CommandExecutorService.executeCommand',
    index=1,
    containing_service=None,
    input_type=_EXECUTIONINPUT,
    output_type=_EXECUTIONOUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDEXECUTORSERVICE)

DESCRIPTOR.services_by_name['CommandExecutorService'] = _COMMANDEXECUTORSERVICE

# @@protoc_insertion_point(module_scope)
