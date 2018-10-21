# Stubs for telegram.bot (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from logging import Logger
from datetime import datetime

from telegram import (Animation, Audio, ChatAction, Contact, Document, InlineQueryResult, InputMedia, LabeledPrice, Location, 
                      MaskPosition, ParseMode, PassportElementError, PhotoSize, ReplyMarkup, ShippingOption, Sticker, 
                      TelegramObject, User, Video, VideoNote, Voice)
from telegram.utils.request import Request

from typing import Any, BinaryIO, Callable, List, Optional, TextIO, Union

def info(func: Callable) -> Callable: ...
def log(func: Callable) -> Callable: ...
def message(func: Callable) -> Callable: ...

class Bot(TelegramObject):
    token: str = ...
    base_url: str = ...
    base_file_url: str = ...
    bot: User = ...
    logger: Logger = ...
    private_key: bytes = ...
    def __init__(self, token: str, base_url: Optional[str] = ..., base_file_url: Optional[str] = ..., request: Optional[Request] = ..., private_key: Optional[bytes] = ..., private_key_password: Optional[bytes] = ...) -> None: ...
    @property
    def request(self) -> Request: ...
    @property
    def id(self) -> int: ...
    @property
    def first_name(self) -> str: ...
    @property
    def last_name(self) -> str: ...
    @property
    def username(self) -> str: ...
    @property
    def name(self) -> str: ...
    def get_me(self, timeout: Optional[float] = ..., **kwargs: Any) -> User: ...
    def send_message(self, chat_id: Union[int, str], text: str, parse_mode: Optional[Union[ParseMode, str]] = ..., disable_web_page_preview: Optional[bool] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def delete_message(self, chat_id: Union[int, str], message_id: int, timeout: Optional[float] = ..., **kwargs: Any): ...
    def forward_message(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, disable_notification: bool = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def send_photo(self, chat_id: Union[int, str], photo: Union[str, BinaryIO, PhotoSize], caption: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., **kwargs: Any): ...
    def send_audio(self, chat_id: Union[int, str], audio: Union[str, BinaryIO, Audio], duration: Optional[int] = ..., performer: Optional[str] = ..., title: Optional[str] = ..., caption: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., thumb: Optional[BinaryIO] = ..., **kwargs: Any): ...
    def send_document(self, chat_id: Union[int, str], document: Union[str, BinaryIO, Document], filename: Optional[str] = ..., caption: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., thumb: Optional[BinaryIO] = ..., **kwargs: Any): ...
    def send_sticker(self, chat_id: Union[int, str], sticker: Union[str, BinaryIO, Sticker], disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., **kwargs: Any): ...
    def send_video(self, chat_id: Union[int, str], video: Union[str, BinaryIO, Video], duration: Optional[int] = ..., caption: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., width: Optional[int] = ..., height: Optional[int] = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., supports_streaming: Optional[bool] = ..., thumb: Optional[BinaryIO] = ..., **kwargs: Any): ...
    def send_video_note(self, chat_id: Union[int, str], video_note: Union[str, BinaryIO, VideoNote], duration: Optional[int] = ..., length: Optional[int] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., thumb: Optional[BinaryIO] = ..., **kwargs: Any): ...
    def send_animation(self, chat_id: Union[int, str], animation: Union[str, BinaryIO, Animation], duration: Optional[int] = ..., width: Optional[int] = ..., height: Optional[int] = ..., thumb: Optional[BinaryIO] = ..., caption: Optional[str] = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., **kwargs: Any): ...
    def send_voice(self, chat_id: Union[int, str], voice: Union[str, BinaryIO, Voice], duration: Optional[int] = ..., caption: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: int = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., **kwargs: Any): ...
    def send_media_group(self, chat_id: Union[int, str], media: List[InputMedia], disable_notification: Optional[bool] = ..., reply_to_message_id: Optional[int] = ..., timeout: int = ..., **kwargs: Any): ...
    def send_location(self, chat_id: Union[int, str], latitude: Optional[float] = ..., longitude: Optional[float] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., location: Optional[Location] = ..., live_period: Optional[int] = ..., **kwargs: Any): ...
    def edit_message_live_location(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., latitude: Optional[float] = ..., longitude: Optional[float] = ..., location: Optional[Location] = ..., reply_markup: Optional[ReplyMarkup] = ..., **kwargs: Any): ...
    def stop_message_live_location(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., **kwargs: Any): ...
    def send_venue(self, chat_id: Union[int, str], latitude: Optional[float] = ..., longitude: Optional[float] = ..., title: Optional[str] = ..., address: Optional[str] = ..., foursquare_id: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., venue: Optional[str] = ..., foursquare_type: Optional[str] = ..., **kwargs: Any): ...
    def send_contact(self, chat_id: Union[int, str], phone_number: Optional[str] = ..., first_name: Optional[str] = ..., last_name: Optional[str] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., contact: Optional[Contact] = ..., vcard: Optional[str] = ..., **kwargs: Any): ...
    def send_game(self, chat_id: Union[int, str], game_short_name: str, disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def send_chat_action(self, chat_id: Union[int, str], action: ChatAction, timeout: Optional[float] = ..., **kwargs: Any): ...
    def answer_inline_query(self, inline_query_id: str, results: List[InlineQueryResult], cache_time: int = ..., is_personal: Optional[bool] = ..., next_offset: Optional[str] = ..., switch_pm_text: Optional[Any] = ..., switch_pm_parameter: Optional[Any] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_user_profile_photos(self, user_id: int, offset: Optional[int] = ..., limit: int = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_file(self, file_id: Union[str, Audio, Document, PhotoSize, Sticker, Video, VideoNote, Voice], timeout: Optional[float] = ..., **kwargs: Any): ...
    def kick_chat_member(self, chat_id: Union[int, str], user_id: int, timeout: Optional[float] = ..., until_date: Optional[Union[int, datetime]] = ..., **kwargs: Any): ...
    def unban_chat_member(self, chat_id: Union[int, str], user_id: int, timeout: Optional[float] = ..., **kwargs: Any): ...
    def answer_callback_query(self, callback_query_id: str, text: Optional[str] = ..., show_alert: bool = ..., url: Optional[str] = ..., cache_time: Optional[int] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def edit_message_text(self, text: str, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., disable_web_page_preview: Optional[bool] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def edit_message_caption(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., caption: Optional[str] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., parse_mode: Optional[Union[ParseMode, str]] = ..., **kwargs: Any): ...
    def edit_message_media(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., media: Optional[InputMedia] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def edit_message_reply_markup(self, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_updates(self, offset: Optional[int] = ..., limit: int = ..., timeout: int = ..., read_latency: float = ..., allowed_updates: Optional[List[str]] = ..., **kwargs: Any): ...
    def set_webhook(self, url: Optional[str] = ..., certificate: Optional[TextIO] = ..., timeout: Optional[float] = ..., max_connections: int = ..., allowed_updates: Optional[List[str]] = ..., **kwargs: Any): ...
    def delete_webhook(self, timeout: Optional[float] = ..., **kwargs: Any): ...
    def leave_chat(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_chat(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_chat_administrators(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_chat_members_count(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_chat_member(self, chat_id: Union[int, str], user_id: int, timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_chat_sticker_set(self, chat_id: Union[int, str], sticker_set_name: str, timeout: Optional[float] = ..., **kwargs: Any): ...
    def delete_chat_sticker_set(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_webhook_info(self, timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_game_score(self, user_id: int, score: int, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., force: Optional[bool] = ..., disable_edit_message: Optional[bool] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_game_high_scores(self, user_id: int, chat_id: Optional[Union[int, str]] = ..., message_id: Optional[int] = ..., inline_message_id: Optional[int] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def send_invoice(self, chat_id: Union[int, str], title: str, description: str, payload: str, provider_token: str, start_parameter: str, currency: str, prices: List[LabeledPrice], photo_url: Optional[str] = ..., photo_size: Optional[str] = ..., photo_width: Optional[int] = ..., photo_height: Optional[int] = ..., need_name: Optional[bool] = ..., need_phone_number: Optional[bool] = ..., need_email: Optional[bool] = ..., need_shipping_address: Optional[bool] = ..., is_flexible: Optional[bool] = ..., disable_notification: bool = ..., reply_to_message_id: Optional[int] = ..., reply_markup: Optional[ReplyMarkup] = ..., provider_data: Optional[object] = ..., send_phone_number_to_provider: Optional[bool] = ..., send_email_to_provider: Optional[bool] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def answer_shipping_query(self, shipping_query_id: str, ok: bool, shipping_options: Optional[List[ShippingOption]] = ..., error_message: Optional[str] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def answer_pre_checkout_query(self, pre_checkout_query_id: str, ok: bool, error_message: Optional[str] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def restrict_chat_member(self, chat_id: Union[int, str], user_id: int, until_date: Optional[Union[int, datetime]] = ..., can_send_messages: Optional[bool] = ..., can_send_media_messages: Optional[bool] = ..., can_send_other_messages: Optional[bool] = ..., can_add_web_page_previews: Optional[bool] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def promote_chat_member(self, chat_id: Union[int, str], user_id: int, can_change_info: Optional[bool] = ..., can_post_messages: Optional[bool] = ..., can_edit_messages: Optional[bool] = ..., can_delete_messages: Optional[bool] = ..., can_invite_users: Optional[bool] = ..., can_restrict_members: Optional[bool] = ..., can_pin_messages: Optional[bool] = ..., can_promote_members: Optional[bool] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def export_chat_invite_link(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_chat_photo(self, chat_id: Union[int, str], photo: Union[str, BinaryIO, PhotoSize], timeout: Optional[float] = ..., **kwargs: Any): ...
    def delete_chat_photo(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_chat_title(self, chat_id: Union[int, str], title: str, timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_chat_description(self, chat_id: Union[int, str], description: str, timeout: Optional[float] = ..., **kwargs: Any): ...
    def pin_chat_message(self, chat_id: Union[int, str], message_id: int, disable_notification: Optional[bool] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def unpin_chat_message(self, chat_id: Union[int, str], timeout: Optional[float] = ..., **kwargs: Any): ...
    def get_sticker_set(self, name: str, timeout: Optional[float] = ..., **kwargs: Any): ...
    def upload_sticker_file(self, user_id: int, png_sticker: Union[str, BinaryIO, Sticker], timeout: Optional[float] = ..., **kwargs: Any): ...
    def create_new_sticker_set(self, user_id: int, name: str, title: str, png_sticker: Union[str, BinaryIO, Sticker], emojis: str, contains_masks: Optional[bool] = ..., mask_position: Optional[MaskPosition] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def add_sticker_to_set(self, user_id: int, name: str, png_sticker: Union[str, BinaryIO, Sticker], emojis: str, mask_position: Optional[MaskPosition] = ..., timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_sticker_position_in_set(self, sticker: Union[str, BinaryIO, Sticker], position: int, timeout: Optional[float] = ..., **kwargs: Any): ...
    def delete_sticker_from_set(self, sticker: Union[str, BinaryIO, Sticker], timeout: Optional[float] = ..., **kwargs: Any): ...
    def set_passport_data_errors(self, user_id: int, errors: List[PassportElementError], timeout: Optional[float] = ..., **kwargs: Any): ...
    def to_dict(self): ...
    def __reduce__(self): ...
