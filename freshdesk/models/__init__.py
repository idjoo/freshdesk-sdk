"""Contains all the data models used in inputs/outputs"""

from .conversations import Conversations
from .create_reply_requests import CreateReplyRequests
from .ticket_base import TicketBase

__all__ = (
    "Conversations",
    "CreateReplyRequests",
    "TicketBase",
)
