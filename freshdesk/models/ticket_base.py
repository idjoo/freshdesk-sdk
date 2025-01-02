import datetime
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="TicketBase")


@_attrs_define
class TicketBase:
    """
    Attributes:
        attachments (Union[Unset, list[File]]): Ticket attachments. The total size of these attachments cannot exceed
            20MB.
        cc_emails (Union[Unset, list[str]]): Email address added in the 'cc' field of the incoming ticket email.
        company_id (Union[Unset, float]): Company ID of the requester. This attribute can only be set if the Multiple
            Companies feature is enabled (Estate plan and above).
        created_at (Union[Unset, datetime.datetime]): Ticket creation timestamp.
        deleted (Union[Unset, bool]): Set to true if the ticket has been deleted/trashed. Deleted tickets will not be
            displayed in any views except the "deleted" filter.
        description (Union[Unset, str]): HTML content of the ticket.
        description_text (Union[Unset, str]): Content of the ticket in plain text.
        due_by (Union[Unset, datetime.datetime]): Timestamp that denotes when the ticket is due to be resolved.
        email (Union[Unset, str]): Email address of the requester. If no contact exists with this email address in
            Freshdesk, it will be added as a new contact.
        email_config_id (Union[Unset, float]): ID of email config which is used for this ticket. (i.e.,
            support@yourcompany.com/sales@yourcompany.com).
        facebook_id (Union[Unset, str]): Facebook ID of the requester. A contact should exist with this facebook_id in
            Freshdesk.
        fr_due_by (Union[Unset, datetime.datetime]): Timestamp that denotes when the first response is due.
        fr_escalated (Union[Unset, bool]): Set to true if the ticket has been escalated as the result of first response
            time being breached.
        fwd_emails (Union[Unset, list[str]]): Email address(e)s added while forwarding a ticket.
        group_id (Union[Unset, float]): ID of the group to which the ticket has been assigned.
        id (Union[Unset, float]): Unique ID of the ticket.
        is_escalated (Union[Unset, bool]): Set to true if the ticket has been escalated for any reason.
        name (Union[Unset, str]): Name of the requester.
        phone (Union[Unset, str]): Phone number of the requester. If no contact exists with this phone number in
            Freshdesk, it will be added as a new contact. If the phone number is set and the email address is not, then the
            name attribute is mandatory.
        priority (Union[Unset, float]): Priority of the ticket.
        product_id (Union[Unset, float]): ID of the product to which the ticket is associated. It will be ignored if the
            email_config_id attribute is set in the request.
        reply_cc_emails (Union[Unset, list[str]]): Email address added while replying to a ticket.
        requester_id (Union[Unset, str]): User ID of the requester. For existing contacts, the requester_id can be
            passed instead of the requester's email.
        responder_id (Union[Unset, float]): ID of the agent to whom the ticket has been assigned.
        source (Union[Unset, float]): The channel through which the ticket was created.
        spam (Union[Unset, bool]): Set to true if the ticket has been marked as spam.
        status (Union[Unset, float]): Status of the ticket.
        subject (Union[Unset, str]): Subject of the ticket.
        tags (Union[Unset, list[str]]): Tags that have been associated with the ticket.
        to_emails (Union[Unset, list[str]]): Email addresses to which the ticket was originally sent.
        twitter_id (Union[Unset, str]): Twitter handle of the requester. If no contact exists with this handle in
            Freshdesk, it will be added as a new contact.
        type_ (Union[Unset, str]): Helps categorize the ticket according to the different kinds of issues your support
            team deals with.
        updated_at (Union[Unset, datetime.datetime]): Ticket updated timestamp.
    """

    attachments: Union[Unset, list[File]] = UNSET
    cc_emails: Union[Unset, list[str]] = UNSET
    company_id: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    description_text: Union[Unset, str] = UNSET
    due_by: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    email_config_id: Union[Unset, float] = UNSET
    facebook_id: Union[Unset, str] = UNSET
    fr_due_by: Union[Unset, datetime.datetime] = UNSET
    fr_escalated: Union[Unset, bool] = UNSET
    fwd_emails: Union[Unset, list[str]] = UNSET
    group_id: Union[Unset, float] = UNSET
    id: Union[Unset, float] = UNSET
    is_escalated: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    priority: Union[Unset, float] = UNSET
    product_id: Union[Unset, float] = UNSET
    reply_cc_emails: Union[Unset, list[str]] = UNSET
    requester_id: Union[Unset, str] = UNSET
    responder_id: Union[Unset, float] = UNSET
    source: Union[Unset, float] = UNSET
    spam: Union[Unset, bool] = UNSET
    status: Union[Unset, float] = UNSET
    subject: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    to_emails: Union[Unset, list[str]] = UNSET
    twitter_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: Union[Unset, list[FileJsonType]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_tuple()

                attachments.append(attachments_item)

        cc_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cc_emails, Unset):
            cc_emails = self.cc_emails

        company_id = self.company_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted = self.deleted

        description = self.description

        description_text = self.description_text

        due_by: Union[Unset, str] = UNSET
        if not isinstance(self.due_by, Unset):
            due_by = self.due_by.isoformat()

        email = self.email

        email_config_id = self.email_config_id

        facebook_id = self.facebook_id

        fr_due_by: Union[Unset, str] = UNSET
        if not isinstance(self.fr_due_by, Unset):
            fr_due_by = self.fr_due_by.isoformat()

        fr_escalated = self.fr_escalated

        fwd_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fwd_emails, Unset):
            fwd_emails = self.fwd_emails

        group_id = self.group_id

        id = self.id

        is_escalated = self.is_escalated

        name = self.name

        phone = self.phone

        priority = self.priority

        product_id = self.product_id

        reply_cc_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reply_cc_emails, Unset):
            reply_cc_emails = self.reply_cc_emails

        requester_id = self.requester_id

        responder_id = self.responder_id

        source = self.source

        spam = self.spam

        status = self.status

        subject = self.subject

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        to_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.to_emails, Unset):
            to_emails = self.to_emails

        twitter_id = self.twitter_id

        type_ = self.type_

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if cc_emails is not UNSET:
            field_dict["cc_emails"] = cc_emails
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if description is not UNSET:
            field_dict["description"] = description
        if description_text is not UNSET:
            field_dict["description_text"] = description_text
        if due_by is not UNSET:
            field_dict["due_by"] = due_by
        if email is not UNSET:
            field_dict["email"] = email
        if email_config_id is not UNSET:
            field_dict["email_config_id"] = email_config_id
        if facebook_id is not UNSET:
            field_dict["facebook_id"] = facebook_id
        if fr_due_by is not UNSET:
            field_dict["fr_due_by"] = fr_due_by
        if fr_escalated is not UNSET:
            field_dict["fr_escalated"] = fr_escalated
        if fwd_emails is not UNSET:
            field_dict["fwd_emails"] = fwd_emails
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_escalated is not UNSET:
            field_dict["is_escalated"] = is_escalated
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if priority is not UNSET:
            field_dict["priority"] = priority
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if reply_cc_emails is not UNSET:
            field_dict["reply_cc_emails"] = reply_cc_emails
        if requester_id is not UNSET:
            field_dict["requester_id"] = requester_id
        if responder_id is not UNSET:
            field_dict["responder_id"] = responder_id
        if source is not UNSET:
            field_dict["source"] = source
        if spam is not UNSET:
            field_dict["spam"] = spam
        if status is not UNSET:
            field_dict["status"] = status
        if subject is not UNSET:
            field_dict["subject"] = subject
        if tags is not UNSET:
            field_dict["tags"] = tags
        if to_emails is not UNSET:
            field_dict["to_emails"] = to_emails
        if twitter_id is not UNSET:
            field_dict["twitter_id"] = twitter_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = File(payload=BytesIO(attachments_item_data))

            attachments.append(attachments_item)

        cc_emails = cast(list[str], d.pop("cc_emails", UNSET))

        company_id = d.pop("company_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        deleted = d.pop("deleted", UNSET)

        description = d.pop("description", UNSET)

        description_text = d.pop("description_text", UNSET)

        _due_by = d.pop("due_by", UNSET)
        due_by: Union[Unset, datetime.datetime]
        if isinstance(_due_by, Unset):
            due_by = UNSET
        else:
            due_by = isoparse(_due_by)

        email = d.pop("email", UNSET)

        email_config_id = d.pop("email_config_id", UNSET)

        facebook_id = d.pop("facebook_id", UNSET)

        _fr_due_by = d.pop("fr_due_by", UNSET)
        fr_due_by: Union[Unset, datetime.datetime]
        if isinstance(_fr_due_by, Unset):
            fr_due_by = UNSET
        else:
            fr_due_by = isoparse(_fr_due_by)

        fr_escalated = d.pop("fr_escalated", UNSET)

        fwd_emails = cast(list[str], d.pop("fwd_emails", UNSET))

        group_id = d.pop("group_id", UNSET)

        id = d.pop("id", UNSET)

        is_escalated = d.pop("is_escalated", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        priority = d.pop("priority", UNSET)

        product_id = d.pop("product_id", UNSET)

        reply_cc_emails = cast(list[str], d.pop("reply_cc_emails", UNSET))

        requester_id = d.pop("requester_id", UNSET)

        responder_id = d.pop("responder_id", UNSET)

        source = d.pop("source", UNSET)

        spam = d.pop("spam", UNSET)

        status = d.pop("status", UNSET)

        subject = d.pop("subject", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        to_emails = cast(list[str], d.pop("to_emails", UNSET))

        twitter_id = d.pop("twitter_id", UNSET)

        type_ = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        ticket_base = cls(
            attachments=attachments,
            cc_emails=cc_emails,
            company_id=company_id,
            created_at=created_at,
            deleted=deleted,
            description=description,
            description_text=description_text,
            due_by=due_by,
            email=email,
            email_config_id=email_config_id,
            facebook_id=facebook_id,
            fr_due_by=fr_due_by,
            fr_escalated=fr_escalated,
            fwd_emails=fwd_emails,
            group_id=group_id,
            id=id,
            is_escalated=is_escalated,
            name=name,
            phone=phone,
            priority=priority,
            product_id=product_id,
            reply_cc_emails=reply_cc_emails,
            requester_id=requester_id,
            responder_id=responder_id,
            source=source,
            spam=spam,
            status=status,
            subject=subject,
            tags=tags,
            to_emails=to_emails,
            twitter_id=twitter_id,
            type_=type_,
            updated_at=updated_at,
        )

        ticket_base.additional_properties = d
        return ticket_base

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
