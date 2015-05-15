# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressbook.proto',
  package='',
  serialized_pb=_b('\n\x11\x61\x64\x64ressbook.proto\")\n\x0b\x41\x64\x64ressBook\x12\x1a\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x08.Contact\"2\n\x07\x41\x64\x64ress\x12\x15\n\raddress_lines\x18\x01 \x03(\t\x12\x10\n\x08postcode\x18\x02 \x01(\t\"j\n\x07\x43ontact\x12\x12\n\nfirst_name\x18\x01 \x02(\t\x12\x11\n\tlast_name\x18\x02 \x02(\t\x12\x19\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x08.Address\x12\x1d\n\rphone_numbers\x18\x04 \x03(\x0b\x32\x06.Phone\"1\n\x05Phone\x12\x18\n\x04type\x18\x01 \x01(\x0e\x32\n.PhoneType\x12\x0e\n\x06number\x18\x02 \x01(\t\"*\n\x0cSearchResult\x12\x1a\n\x08\x63ontacts\x18\x01 \x03(\x0b\x32\x08.Contact*%\n\tPhoneType\x12\n\n\x06MOBILE\x10\x01\x12\x0c\n\x08LANDLINE\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LANDLINE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=319,
  serialized_end=356,
)
_sym_db.RegisterEnumDescriptor(_PHONETYPE)

PhoneType = enum_type_wrapper.EnumTypeWrapper(_PHONETYPE)
MOBILE = 1
LANDLINE = 2



_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contacts', full_name='AddressBook.contacts', index=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=62,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_lines', full_name='Address.address_lines', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postcode', full_name='Address.postcode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=114,
)


_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='Contact.first_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='Contact.last_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='Contact.address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone_numbers', full_name='Contact.phone_numbers', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=222,
)


_PHONE = _descriptor.Descriptor(
  name='Phone',
  full_name='Phone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Phone.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='Phone.number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=273,
)


_SEARCHRESULT = _descriptor.Descriptor(
  name='SearchResult',
  full_name='SearchResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contacts', full_name='SearchResult.contacts', index=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=317,
)

_ADDRESSBOOK.fields_by_name['contacts'].message_type = _CONTACT
_CONTACT.fields_by_name['address'].message_type = _ADDRESS
_CONTACT.fields_by_name['phone_numbers'].message_type = _PHONE
_PHONE.fields_by_name['type'].enum_type = _PHONETYPE
_SEARCHRESULT.fields_by_name['contacts'].message_type = _CONTACT
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
DESCRIPTOR.message_types_by_name['Phone'] = _PHONE
DESCRIPTOR.message_types_by_name['SearchResult'] = _SEARCHRESULT
DESCRIPTOR.enum_types_by_name['PhoneType'] = _PHONETYPE

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESS,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  ))
_sym_db.RegisterMessage(Address)

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), dict(
  DESCRIPTOR = _CONTACT,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Contact)
  ))
_sym_db.RegisterMessage(Contact)

Phone = _reflection.GeneratedProtocolMessageType('Phone', (_message.Message,), dict(
  DESCRIPTOR = _PHONE,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:Phone)
  ))
_sym_db.RegisterMessage(Phone)

SearchResult = _reflection.GeneratedProtocolMessageType('SearchResult', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRESULT,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:SearchResult)
  ))
_sym_db.RegisterMessage(SearchResult)


# @@protoc_insertion_point(module_scope)
