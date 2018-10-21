# Stubs for telegram.inline.inlinequeryresultgif (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from telegram import InlineQueryResult
from typing import Any, Optional

class InlineQueryResultGif(InlineQueryResult):
    gif_url: Any = ...
    thumb_url: Any = ...
    gif_width: Any = ...
    gif_height: Any = ...
    gif_duration: Any = ...
    title: Any = ...
    caption: Any = ...
    parse_mode: Any = ...
    reply_markup: Any = ...
    input_message_content: Any = ...
    def __init__(self, id: Any, gif_url: Any, thumb_url: Any, gif_width: Optional[Any] = ..., gif_height: Optional[Any] = ..., title: Optional[Any] = ..., caption: Optional[Any] = ..., reply_markup: Optional[Any] = ..., input_message_content: Optional[Any] = ..., gif_duration: Optional[Any] = ..., parse_mode: Optional[Any] = ..., **kwargs: Any) -> None: ...
