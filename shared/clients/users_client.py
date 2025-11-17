import httpx

from shared.lib.constants import (
    INTERNAL_API_KEY,
    INTERNAL_API_KEY_HEADER_NAME,
    USERS_API_URL,
)
from shared.models.status_response_dto import StatusResponse
from shared.models.user_dto import User


async def get_user_by_ulid_async(user_ulid: str) -> StatusResponse[User]:
    async with httpx.AsyncClient() as client:
        user_response = await client.get(
            f"{USERS_API_URL}/api/v1/users/{user_ulid}",
            headers={INTERNAL_API_KEY_HEADER_NAME: INTERNAL_API_KEY},
        )

        user_response.raise_for_status()

        return StatusResponse[User](**user_response.json())


async def create_user_by_ulid_async() -> StatusResponse[User]:
    async with httpx.AsyncClient() as client:
        return await create_user_with_client_async(client)


async def create_user_with_client_async(
    client: httpx.AsyncClient,
) -> StatusResponse[User]:
    create_response = await client.post(
        f"{USERS_API_URL}/api/v1/users",
        json={},
        headers={INTERNAL_API_KEY_HEADER_NAME: INTERNAL_API_KEY},
    )

    create_response.raise_for_status()

    return StatusResponse[User](**create_response.json())


async def delete_user_with_client_async(
    client: httpx.AsyncClient, user_ulid: str
) -> StatusResponse:
    delete_response = await client.delete(
        f"{USERS_API_URL}/api/v1/users/{user_ulid}",
        headers={INTERNAL_API_KEY_HEADER_NAME: INTERNAL_API_KEY},
    )

    delete_response.raise_for_status()

    return StatusResponse(**delete_response.json())
