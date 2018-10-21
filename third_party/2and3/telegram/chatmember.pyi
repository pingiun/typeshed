# Stubs for telegram.chatmember (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from telegram import TelegramObject
from typing import Any, Optional

class ChatMember(TelegramObject):
    ADMINISTRATOR: str = ...
    CREATOR: str = ...
    KICKED: str = ...
    LEFT: str = ...
    MEMBER: str = ...
    RESTRICTED: str = ...
    user: Any = ...
    status: Any = ...
    until_date: Any = ...
    can_be_edited: Any = ...
    can_change_info: Any = ...
    can_post_messages: Any = ...
    can_edit_messages: Any = ...
    can_delete_messages: Any = ...
    can_invite_users: Any = ...
    can_restrict_members: Any = ...
    can_pin_messages: Any = ...
    can_promote_members: Any = ...
    can_send_messages: Any = ...
    can_send_media_messages: Any = ...
    can_send_other_messages: Any = ...
    can_add_web_page_previews: Any = ...
    def __init__(self, user: Any, status: Any, until_date: Optional[Any] = ..., can_be_edited: Optional[Any] = ..., can_change_info: Optional[Any] = ..., can_post_messages: Optional[Any] = ..., can_edit_messages: Optional[Any] = ..., can_delete_messages: Optional[Any] = ..., can_invite_users: Optional[Any] = ..., can_restrict_members: Optional[Any] = ..., can_pin_messages: Optional[Any] = ..., can_promote_members: Optional[Any] = ..., can_send_messages: Optional[Any] = ..., can_send_media_messages: Optional[Any] = ..., can_send_other_messages: Optional[Any] = ..., can_add_web_page_previews: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @classmethod
    def de_json(cls, data: Any, bot: Any): ...
    def to_dict(self): ...
