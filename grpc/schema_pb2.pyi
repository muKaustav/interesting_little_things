from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoTask(_message.Message):
    __slots__ = ["video_url", "watermark_url", "x_offset", "y_offset", "email", "current_epoch"]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    WATERMARK_URL_FIELD_NUMBER: _ClassVar[int]
    X_OFFSET_FIELD_NUMBER: _ClassVar[int]
    Y_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_EPOCH_FIELD_NUMBER: _ClassVar[int]
    video_url: str
    watermark_url: str
    x_offset: int
    y_offset: int
    email: str
    current_epoch: int
    def __init__(self, video_url: _Optional[str] = ..., watermark_url: _Optional[str] = ..., x_offset: _Optional[int] = ..., y_offset: _Optional[int] = ..., email: _Optional[str] = ..., current_epoch: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["unique_id", "status"]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    unique_id: str
    status: str
    def __init__(self, unique_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...
