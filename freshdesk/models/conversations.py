import datetime
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="Conversations")


@_attrs_define
class Conversations:
    """
    Attributes:
        attachments (Union[Unset, list[File]]): Ticket attachments. The total size of these attachments cannot exceed
            20MB.
        body (Union[Unset, str]): Content of the conversation in HTML.
        body_text (Union[Unset, str]): Content of the conversation in plain text.
        created_at (Union[Unset, datetime.datetime]): Conversation creation timestamp.
        id (Union[Unset, float]): ID of the conversation.
        incoming (Union[Unset, bool]): Set to true if a particular conversation should appear as being created from
            outside (i.e., not through web portal).
        last_edited_at (Union[Unset, datetime.datetime]): Timestamp when the conversation last edited.
        last_edited_user_id (Union[Unset, datetime.datetime]): ID of the agent who has last edited the conversation.
        private (Union[Unset, bool]): Set to true if the note is private.
        source (Union[Unset, float]): Denotes the type of the conversation.
        support_email (Union[Unset, str]): Email address from which the reply is sent. For notes, this value will be
            null.
        ticket_id (Union[Unset, float]): ID of the ticket to which this conversation is being added.
        to_emails (Union[Unset, list[str]]): Email addresses of agents/users who need to be notified about this
            conversation.
        updated_at (Union[Unset, datetime.datetime]): Conversation updated timestamp.
        user_id (Union[Unset, float]): ID of the agent/user who is adding the conversation.
    """

    attachments: Union[Unset, list[File]] = UNSET
    body: Union[Unset, str] = UNSET
    body_text: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, float] = UNSET
    incoming: Union[Unset, bool] = UNSET
    last_edited_at: Union[Unset, datetime.datetime] = UNSET
    last_edited_user_id: Union[Unset, datetime.datetime] = UNSET
    private: Union[Unset, bool] = UNSET
    source: Union[Unset, float] = UNSET
    support_email: Union[Unset, str] = UNSET
    ticket_id: Union[Unset, float] = UNSET
    to_emails: Union[Unset, list[str]] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: Union[Unset, list[FileJsonType]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_tuple()

                attachments.append(attachments_item)

        body = self.body

        body_text = self.body_text

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        incoming = self.incoming

        last_edited_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_edited_at, Unset):
            last_edited_at = self.last_edited_at.isoformat()

        last_edited_user_id: Union[Unset, str] = UNSET
        if not isinstance(self.last_edited_user_id, Unset):
            last_edited_user_id = self.last_edited_user_id.isoformat()

        private = self.private

        source = self.source

        support_email = self.support_email

        ticket_id = self.ticket_id

        to_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.to_emails, Unset):
            to_emails = self.to_emails

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if body is not UNSET:
            field_dict["body"] = body
        if body_text is not UNSET:
            field_dict["body_text"] = body_text
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if incoming is not UNSET:
            field_dict["incoming"] = incoming
        if last_edited_at is not UNSET:
            field_dict["last_edited_at"] = last_edited_at
        if last_edited_user_id is not UNSET:
            field_dict["last_edited_user_id"] = last_edited_user_id
        if private is not UNSET:
            field_dict["private"] = private
        if source is not UNSET:
            field_dict["source"] = source
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if ticket_id is not UNSET:
            field_dict["ticket_id"] = ticket_id
        if to_emails is not UNSET:
            field_dict["to_emails"] = to_emails
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = File(payload=BytesIO(attachments_item_data))

            attachments.append(attachments_item)

        body = d.pop("body", UNSET)

        body_text = d.pop("body_text", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        incoming = d.pop("incoming", UNSET)

        _last_edited_at = d.pop("last_edited_at", UNSET)
        last_edited_at: Union[Unset, datetime.datetime]
        if isinstance(_last_edited_at, Unset):
            last_edited_at = UNSET
        else:
            last_edited_at = isoparse(_last_edited_at)

        _last_edited_user_id = d.pop("last_edited_user_id", UNSET)
        last_edited_user_id: Union[Unset, datetime.datetime]
        if isinstance(_last_edited_user_id, Unset):
            last_edited_user_id = UNSET
        else:
            last_edited_user_id = isoparse(_last_edited_user_id)

        private = d.pop("private", UNSET)

        source = d.pop("source", UNSET)

        support_email = d.pop("support_email", UNSET)

        ticket_id = d.pop("ticket_id", UNSET)

        to_emails = cast(list[str], d.pop("to_emails", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        conversations = cls(
            attachments=attachments,
            body=body,
            body_text=body_text,
            created_at=created_at,
            id=id,
            incoming=incoming,
            last_edited_at=last_edited_at,
            last_edited_user_id=last_edited_user_id,
            private=private,
            source=source,
            support_email=support_email,
            ticket_id=ticket_id,
            to_emails=to_emails,
            updated_at=updated_at,
            user_id=user_id,
        )

        conversations.additional_properties = d
        return conversations

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
