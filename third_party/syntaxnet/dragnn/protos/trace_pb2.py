# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dragnn/protos/trace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dragnn.protos import data_pb2 as dragnn_dot_protos_dot_data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dragnn/protos/trace.proto',
  package='syntaxnet.dragnn',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x64ragnn/protos/trace.proto\x12\x10syntaxnet.dragnn\x1a\x18\x64ragnn/protos/data.proto\"^\n\x18\x46ixedFeatureChannelTrace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x0bvalue_trace\x18\x02 \x03(\x0b\x32\x1f.syntaxnet.dragnn.FixedFeatures\"\xa9\x01\n\x19LinkedFeatureChannelTrace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10source_component\x18\x02 \x01(\t\x12\x19\n\x11source_translator\x18\x03 \x01(\t\x12\x14\n\x0csource_layer\x18\x04 \x01(\t\x12\x33\n\x0bvalue_trace\x18\x05 \x03(\x0b\x32\x1e.syntaxnet.dragnn.LinkFeatures\"\x8b\x02\n\x12\x43omponentStepTrace\x12\x0f\n\x07\x63\x61ption\x18\x01 \x01(\t\x12G\n\x13\x66ixed_feature_trace\x18\x02 \x03(\x0b\x32*.syntaxnet.dragnn.FixedFeatureChannelTrace\x12I\n\x14linked_feature_trace\x18\x03 \x03(\x0b\x32+.syntaxnet.dragnn.LinkedFeatureChannelTrace\x12\x1b\n\x13html_representation\x18\x04 \x01(\t\x12\x15\n\routcome_score\x18\x05 \x03(\x01\x12\x1c\n\rstep_finished\x18\x06 \x01(\x08:\x05\x66\x61lse\"X\n\x0e\x43omponentTrace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\nstep_trace\x18\x02 \x03(\x0b\x32$.syntaxnet.dragnn.ComponentStepTrace\"H\n\x0bMasterTrace\x12\x39\n\x0f\x63omponent_trace\x18\x01 \x03(\x0b\x32 .syntaxnet.dragnn.ComponentTrace\"B\n\x0b\x44ragnnTrace\x12\x33\n\x0cmaster_trace\x18\x01 \x03(\x0b\x32\x1d.syntaxnet.dragnn.MasterTrace')
  ,
  dependencies=[dragnn_dot_protos_dot_data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FIXEDFEATURECHANNELTRACE = _descriptor.Descriptor(
  name='FixedFeatureChannelTrace',
  full_name='syntaxnet.dragnn.FixedFeatureChannelTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='syntaxnet.dragnn.FixedFeatureChannelTrace.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_trace', full_name='syntaxnet.dragnn.FixedFeatureChannelTrace.value_trace', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=167,
)


_LINKEDFEATURECHANNELTRACE = _descriptor.Descriptor(
  name='LinkedFeatureChannelTrace',
  full_name='syntaxnet.dragnn.LinkedFeatureChannelTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='syntaxnet.dragnn.LinkedFeatureChannelTrace.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_component', full_name='syntaxnet.dragnn.LinkedFeatureChannelTrace.source_component', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_translator', full_name='syntaxnet.dragnn.LinkedFeatureChannelTrace.source_translator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_layer', full_name='syntaxnet.dragnn.LinkedFeatureChannelTrace.source_layer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_trace', full_name='syntaxnet.dragnn.LinkedFeatureChannelTrace.value_trace', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=339,
)


_COMPONENTSTEPTRACE = _descriptor.Descriptor(
  name='ComponentStepTrace',
  full_name='syntaxnet.dragnn.ComponentStepTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='caption', full_name='syntaxnet.dragnn.ComponentStepTrace.caption', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed_feature_trace', full_name='syntaxnet.dragnn.ComponentStepTrace.fixed_feature_trace', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linked_feature_trace', full_name='syntaxnet.dragnn.ComponentStepTrace.linked_feature_trace', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='html_representation', full_name='syntaxnet.dragnn.ComponentStepTrace.html_representation', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outcome_score', full_name='syntaxnet.dragnn.ComponentStepTrace.outcome_score', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_finished', full_name='syntaxnet.dragnn.ComponentStepTrace.step_finished', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=609,
)


_COMPONENTTRACE = _descriptor.Descriptor(
  name='ComponentTrace',
  full_name='syntaxnet.dragnn.ComponentTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='syntaxnet.dragnn.ComponentTrace.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_trace', full_name='syntaxnet.dragnn.ComponentTrace.step_trace', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=699,
)


_MASTERTRACE = _descriptor.Descriptor(
  name='MasterTrace',
  full_name='syntaxnet.dragnn.MasterTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component_trace', full_name='syntaxnet.dragnn.MasterTrace.component_trace', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=701,
  serialized_end=773,
)


_DRAGNNTRACE = _descriptor.Descriptor(
  name='DragnnTrace',
  full_name='syntaxnet.dragnn.DragnnTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='master_trace', full_name='syntaxnet.dragnn.DragnnTrace.master_trace', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=841,
)

_FIXEDFEATURECHANNELTRACE.fields_by_name['value_trace'].message_type = dragnn_dot_protos_dot_data__pb2._FIXEDFEATURES
_LINKEDFEATURECHANNELTRACE.fields_by_name['value_trace'].message_type = dragnn_dot_protos_dot_data__pb2._LINKFEATURES
_COMPONENTSTEPTRACE.fields_by_name['fixed_feature_trace'].message_type = _FIXEDFEATURECHANNELTRACE
_COMPONENTSTEPTRACE.fields_by_name['linked_feature_trace'].message_type = _LINKEDFEATURECHANNELTRACE
_COMPONENTTRACE.fields_by_name['step_trace'].message_type = _COMPONENTSTEPTRACE
_MASTERTRACE.fields_by_name['component_trace'].message_type = _COMPONENTTRACE
_DRAGNNTRACE.fields_by_name['master_trace'].message_type = _MASTERTRACE
DESCRIPTOR.message_types_by_name['FixedFeatureChannelTrace'] = _FIXEDFEATURECHANNELTRACE
DESCRIPTOR.message_types_by_name['LinkedFeatureChannelTrace'] = _LINKEDFEATURECHANNELTRACE
DESCRIPTOR.message_types_by_name['ComponentStepTrace'] = _COMPONENTSTEPTRACE
DESCRIPTOR.message_types_by_name['ComponentTrace'] = _COMPONENTTRACE
DESCRIPTOR.message_types_by_name['MasterTrace'] = _MASTERTRACE
DESCRIPTOR.message_types_by_name['DragnnTrace'] = _DRAGNNTRACE

FixedFeatureChannelTrace = _reflection.GeneratedProtocolMessageType('FixedFeatureChannelTrace', (_message.Message,), dict(
  DESCRIPTOR = _FIXEDFEATURECHANNELTRACE,
  __module__ = 'dragnn.protos.trace_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.dragnn.FixedFeatureChannelTrace)
  ))
_sym_db.RegisterMessage(FixedFeatureChannelTrace)

LinkedFeatureChannelTrace = _reflection.GeneratedProtocolMessageType('LinkedFeatureChannelTrace', (_message.Message,), dict(
  DESCRIPTOR = _LINKEDFEATURECHANNELTRACE,
  __module__ = 'dragnn.protos.trace_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.dragnn.LinkedFeatureChannelTrace)
  ))
_sym_db.RegisterMessage(LinkedFeatureChannelTrace)

ComponentStepTrace = _reflection.GeneratedProtocolMessageType('ComponentStepTrace', (_message.Message,), dict(
  DESCRIPTOR = _COMPONENTSTEPTRACE,
  __module__ = 'dragnn.protos.trace_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.dragnn.ComponentStepTrace)
  ))
_sym_db.RegisterMessage(ComponentStepTrace)

ComponentTrace = _reflection.GeneratedProtocolMessageType('ComponentTrace', (_message.Message,), dict(
  DESCRIPTOR = _COMPONENTTRACE,
  __module__ = 'dragnn.protos.trace_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.dragnn.ComponentTrace)
  ))
_sym_db.RegisterMessage(ComponentTrace)

MasterTrace = _reflection.GeneratedProtocolMessageType('MasterTrace', (_message.Message,), dict(
  DESCRIPTOR = _MASTERTRACE,
  __module__ = 'dragnn.protos.trace_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.dragnn.MasterTrace)
  ))
_sym_db.RegisterMessage(MasterTrace)

DragnnTrace = _reflection.GeneratedProtocolMessageType('DragnnTrace', (_message.Message,), dict(
  DESCRIPTOR = _DRAGNNTRACE,
  __module__ = 'dragnn.protos.trace_pb2'
  # @@protoc_insertion_point(class_scope:syntaxnet.dragnn.DragnnTrace)
  ))
_sym_db.RegisterMessage(DragnnTrace)


# @@protoc_insertion_point(module_scope)