# Stubs for telegram.inline.inlinequeryresultaudio (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from telegram import InlineQueryResult
from typing import Any, Optional

class InlineQueryResultAudio(InlineQueryResult):
    audio_url: Any = ...
    title: Any = ...
    performer: Any = ...
    audio_duration: Any = ...
    caption: Any = ...
    parse_mode: Any = ...
    reply_markup: Any = ...
    input_message_content: Any = ...
    def __init__(self, id: Any, audio_url: Any, title: Any, performer: Optional[Any] = ..., audio_duration: Optional[Any] = ..., caption: Optional[Any] = ..., reply_markup: Optional[Any] = ..., input_message_content: Optional[Any] = ..., parse_mode: Optional[Any] = ..., **kwargs: Any) -> None: ...
