# Stubs for telegram.choseninlineresult (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from telegram import TelegramObject
from typing import Any, Optional

class ChosenInlineResult(TelegramObject):
    result_id: Any = ...
    from_user: Any = ...
    query: Any = ...
    location: Any = ...
    inline_message_id: Any = ...
    def __init__(self, result_id: Any, from_user: Any, query: Any, location: Optional[Any] = ..., inline_message_id: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls, data: Any, bot: Any): ...
