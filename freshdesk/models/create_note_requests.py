from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateNoteRequests")


@_attrs_define
class CreateNoteRequests:
    """
    Attributes:
        body (str): Content of the note in HTML format.
        attachments (Union[Unset, list[File]]): Ticket attachments. The total size of these attachments cannot exceed
            20MB.
        bcc_emails (Union[Unset, str]): Email address added in the 'bcc' field of the outgoing ticket email.
        cc_emails (Union[Unset, str]): Email address added in the 'cc' field of the outgoing ticket email.
        from_email (Union[Unset, str]): The email address from which the reply is sent. By default the global support
            email will be used.
        user_id (Union[Unset, str]): ID of the agent who is adding the note.
    """

    body: str
    attachments: Union[Unset, list[File]] = UNSET
    bcc_emails: Union[Unset, str] = UNSET
    cc_emails: Union[Unset, str] = UNSET
    from_email: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        attachments: Union[Unset, list[FileJsonType]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_tuple()

                attachments.append(attachments_item)

        bcc_emails = self.bcc_emails

        cc_emails = self.cc_emails

        from_email = self.from_email

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if bcc_emails is not UNSET:
            field_dict["bcc_emails"] = bcc_emails
        if cc_emails is not UNSET:
            field_dict["cc_emails"] = cc_emails
        if from_email is not UNSET:
            field_dict["from_email"] = from_email
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        body = d.pop("body")

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = File(payload=BytesIO(attachments_item_data))

            attachments.append(attachments_item)

        bcc_emails = d.pop("bcc_emails", UNSET)

        cc_emails = d.pop("cc_emails", UNSET)

        from_email = d.pop("from_email", UNSET)

        user_id = d.pop("user_id", UNSET)

        create_note_requests = cls(
            body=body,
            attachments=attachments,
            bcc_emails=bcc_emails,
            cc_emails=cc_emails,
            from_email=from_email,
            user_id=user_id,
        )

        create_note_requests.additional_properties = d
        return create_note_requests

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
