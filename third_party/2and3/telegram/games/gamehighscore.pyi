# Stubs for telegram.games.gamehighscore (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from telegram import TelegramObject
from typing import Any

class GameHighScore(TelegramObject):
    position: Any = ...
    user: Any = ...
    score: Any = ...
    def __init__(self, position: Any, user: Any, score: Any) -> None: ...
    @classmethod
    def de_json(cls, data: Any, bot: Any): ...
