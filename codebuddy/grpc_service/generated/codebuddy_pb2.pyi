from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetBuddyRequest(_message.Message):
    __slots__ = ["phone_number"]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    def __init__(self, phone_number: _Optional[str] = ...) -> None: ...

class Buddy(_message.Message):
    __slots__ = ["phone_number", "display_name"]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    display_name: str
    def __init__(self, phone_number: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...
