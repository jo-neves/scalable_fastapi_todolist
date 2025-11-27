import httpx

from shared.lib.application_variables import ApplicationVariables
from shared.lib.constants import (
    INTERNAL_API_KEY_HEADER_NAME,
)
from shared.models.status_response_dto import StatusResponse
from shared.models.user_dto import User


async def get_user_by_ulid_async(user_ulid: str, token: str) -> StatusResponse[User]:
    async with httpx.AsyncClient() as client:
        user_response = await client.get(
            f"{ApplicationVariables.USERS_API_PRIVATE_URL()}/api/v1/users/{user_ulid}",
            headers={"Authorization": f"Bearer {token}"},
        )

        user_response.raise_for_status()

        return StatusResponse[User](**user_response.json())


async def delete_user_with_client_async(
    client: httpx.AsyncClient, user_ulid: str
) -> StatusResponse:
    delete_response = await client.delete(
        f"{ApplicationVariables.USERS_API_PRIVATE_URL()}/api/v1/users/{user_ulid}/",
        headers={
            INTERNAL_API_KEY_HEADER_NAME: ApplicationVariables.INTERNAL_API_KEY() or ""
        },
    )

    delete_response.raise_for_status()

    return StatusResponse(**delete_response.json())
