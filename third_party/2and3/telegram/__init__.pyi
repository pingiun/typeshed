# Stubs for telegram (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import TelegramObject as TelegramObject
from .bot import Bot as Bot
from .callbackquery import CallbackQuery as CallbackQuery
from .chat import Chat as Chat
from .chataction import ChatAction as ChatAction
from .chatmember import ChatMember as ChatMember
from .choseninlineresult import ChosenInlineResult as ChosenInlineResult
from .constants import MAX_CAPTION_LENGTH as MAX_CAPTION_LENGTH, MAX_FILESIZE_DOWNLOAD as MAX_FILESIZE_DOWNLOAD, MAX_FILESIZE_UPLOAD as MAX_FILESIZE_UPLOAD, MAX_MESSAGES_PER_MINUTE_PER_GROUP as MAX_MESSAGES_PER_MINUTE_PER_GROUP, MAX_MESSAGES_PER_SECOND as MAX_MESSAGES_PER_SECOND, MAX_MESSAGES_PER_SECOND_PER_CHAT as MAX_MESSAGES_PER_SECOND_PER_CHAT, MAX_MESSAGE_LENGTH as MAX_MESSAGE_LENGTH, SUPPORTED_WEBHOOK_PORTS as SUPPORTED_WEBHOOK_PORTS
from .error import TelegramError as TelegramError
from .files.animation import Animation as Animation
from .files.audio import Audio as Audio
from .files.chatphoto import ChatPhoto as ChatPhoto
from .files.contact import Contact as Contact
from .files.document import Document as Document
from .files.file import File as File
from .files.inputfile import InputFile as InputFile
from .files.inputmedia import InputMedia as InputMedia, InputMediaAnimation as InputMediaAnimation, InputMediaAudio as InputMediaAudio, InputMediaDocument as InputMediaDocument, InputMediaPhoto as InputMediaPhoto, InputMediaVideo as InputMediaVideo
from .files.location import Location as Location
from .files.photosize import PhotoSize as PhotoSize
from .files.sticker import MaskPosition as MaskPosition, Sticker as Sticker, StickerSet as StickerSet
from .files.venue import Venue as Venue
from .files.video import Video as Video
from .files.videonote import VideoNote as VideoNote
from .files.voice import Voice as Voice
from .forcereply import ForceReply as ForceReply
from .games.callbackgame import CallbackGame as CallbackGame
from .games.game import Game as Game
from .games.gamehighscore import GameHighScore as GameHighScore
from .inline.inlinekeyboardbutton import InlineKeyboardButton as InlineKeyboardButton
from .inline.inlinekeyboardmarkup import InlineKeyboardMarkup as InlineKeyboardMarkup
from .inline.inlinequery import InlineQuery as InlineQuery
from .inline.inlinequeryresult import InlineQueryResult as InlineQueryResult
from .inline.inlinequeryresultarticle import InlineQueryResultArticle as InlineQueryResultArticle
from .inline.inlinequeryresultaudio import InlineQueryResultAudio as InlineQueryResultAudio
from .inline.inlinequeryresultcachedaudio import InlineQueryResultCachedAudio as InlineQueryResultCachedAudio
from .inline.inlinequeryresultcacheddocument import InlineQueryResultCachedDocument as InlineQueryResultCachedDocument
from .inline.inlinequeryresultcachedgif import InlineQueryResultCachedGif as InlineQueryResultCachedGif
from .inline.inlinequeryresultcachedmpeg4gif import InlineQueryResultCachedMpeg4Gif as InlineQueryResultCachedMpeg4Gif
from .inline.inlinequeryresultcachedphoto import InlineQueryResultCachedPhoto as InlineQueryResultCachedPhoto
from .inline.inlinequeryresultcachedsticker import InlineQueryResultCachedSticker as InlineQueryResultCachedSticker
from .inline.inlinequeryresultcachedvideo import InlineQueryResultCachedVideo as InlineQueryResultCachedVideo
from .inline.inlinequeryresultcachedvoice import InlineQueryResultCachedVoice as InlineQueryResultCachedVoice
from .inline.inlinequeryresultcontact import InlineQueryResultContact as InlineQueryResultContact
from .inline.inlinequeryresultdocument import InlineQueryResultDocument as InlineQueryResultDocument
from .inline.inlinequeryresultgame import InlineQueryResultGame as InlineQueryResultGame
from .inline.inlinequeryresultgif import InlineQueryResultGif as InlineQueryResultGif
from .inline.inlinequeryresultlocation import InlineQueryResultLocation as InlineQueryResultLocation
from .inline.inlinequeryresultmpeg4gif import InlineQueryResultMpeg4Gif as InlineQueryResultMpeg4Gif
from .inline.inlinequeryresultphoto import InlineQueryResultPhoto as InlineQueryResultPhoto
from .inline.inlinequeryresultvenue import InlineQueryResultVenue as InlineQueryResultVenue
from .inline.inlinequeryresultvideo import InlineQueryResultVideo as InlineQueryResultVideo
from .inline.inlinequeryresultvoice import InlineQueryResultVoice as InlineQueryResultVoice
from .inline.inputcontactmessagecontent import InputContactMessageContent as InputContactMessageContent
from .inline.inputlocationmessagecontent import InputLocationMessageContent as InputLocationMessageContent
from .inline.inputmessagecontent import InputMessageContent as InputMessageContent
from .inline.inputtextmessagecontent import InputTextMessageContent as InputTextMessageContent
from .inline.inputvenuemessagecontent import InputVenueMessageContent as InputVenueMessageContent
from .keyboardbutton import KeyboardButton as KeyboardButton
from .message import Message as Message
from .messageentity import MessageEntity as MessageEntity
from .parsemode import ParseMode as ParseMode
from .passport.credentials import Credentials as Credentials, DataCredentials as DataCredentials, EncryptedCredentials as EncryptedCredentials, FileCredentials as FileCredentials, SecureData as SecureData, TelegramDecryptionError as TelegramDecryptionError
from .passport.data import IdDocumentData as IdDocumentData, PersonalDetails as PersonalDetails, ResidentialAddress as ResidentialAddress
from .passport.encryptedpassportelement import EncryptedPassportElement as EncryptedPassportElement
from .passport.passportdata import PassportData as PassportData
from .passport.passportelementerrors import PassportElementError as PassportElementError, PassportElementErrorDataField as PassportElementErrorDataField, PassportElementErrorFile as PassportElementErrorFile, PassportElementErrorFiles as PassportElementErrorFiles, PassportElementErrorFrontSide as PassportElementErrorFrontSide, PassportElementErrorReverseSide as PassportElementErrorReverseSide, PassportElementErrorSelfie as PassportElementErrorSelfie, PassportElementErrorTranslationFile as PassportElementErrorTranslationFile, PassportElementErrorTranslationFiles as PassportElementErrorTranslationFiles, PassportElementErrorUnspecified as PassportElementErrorUnspecified
from .passport.passportfile import PassportFile as PassportFile
from .payment.invoice import Invoice as Invoice
from .payment.labeledprice import LabeledPrice as LabeledPrice
from .payment.orderinfo import OrderInfo as OrderInfo
from .payment.precheckoutquery import PreCheckoutQuery as PreCheckoutQuery
from .payment.shippingaddress import ShippingAddress as ShippingAddress
from .payment.shippingoption import ShippingOption as ShippingOption
from .payment.shippingquery import ShippingQuery as ShippingQuery
from .payment.successfulpayment import SuccessfulPayment as SuccessfulPayment
from .replykeyboardmarkup import ReplyKeyboardMarkup as ReplyKeyboardMarkup
from .replykeyboardremove import ReplyKeyboardRemove as ReplyKeyboardRemove
from .replymarkup import ReplyMarkup as ReplyMarkup
from .update import Update as Update
from .user import User as User
from .userprofilephotos import UserProfilePhotos as UserProfilePhotos
from .webhookinfo import WebhookInfo as WebhookInfo
