import asyncio

from smartfren_ccai_sdk import Client
from smartfren_ccai_sdk.api.self_care import create_magiclink
from smartfren_ccai_sdk.models import (
    MagicLinkRequest,
    MagicLinkRequestClientData,
    MagicLinkResponse,
)


async def main():
    client = Client(
        base_url="http://tykapi.smartfren.com",
        kid="eyJcmciOiI1ZDFkMzM0YjAwZDA0NjNmNzkzNGQ1MTEiLCJpZCI6IjAxMjRjMDE2YjllMTQyYzRiOWFlMGM1ZjRmYzUyNTU3IiwiaCI6Im11cm11cjY0In0=",
        project_id="smartfren-chatbot-prd",
        secret_id="sf-rsa-tyk-prd",
    )

    async with client as client:
        body = MagicLinkRequest(
            context="customer_portal",
            client_id="agifcjcfiajdcfhkikab",
            client_datetime="2024-10-25 09:27:14",
            delivery_channel="sms",
            delivery_address="8881852264",
            tout=180,
            client_data=MagicLinkRequestClientData(
                customer_name="KHAMDAN NGAZIZ", callback_url=""
            ),
        )

        data: MagicLinkResponse = await create_magiclink.asyncio_detailed(
            client=client, body=body
        )

        print(data)


if __name__ == "__main__":
    asyncio.run(main())
