from tortoise.transactions import in_transaction

from auth_api.data.db_query_utils import select_user_credentials_by_user_ulid_async
from auth_api.data.mapper_utils import data_user_credentials_to_model
from auth_api.data.redis_query_utils import (
    delete_cached_user_credentials_async,
    set_cached_user_credentials_async,
)
from shared.event_models.users import UserCreated
from shared.lib.HTTPException_utils import user_not_found_exception
from shared.lib.redis_utils import get_redis_client


async def handle_user_created_async(dto: UserCreated):
    redis_client = get_redis_client()

    data_user_credentials = await select_user_credentials_by_user_ulid_async(
        dto.temp_user_ulid
    )
    if data_user_credentials is None:
        raise user_not_found_exception(dto.temp_user_ulid + " [TEMP]")

    async with in_transaction():
        data_user_credentials.user_ulid = dto.final_user_ulid
        await data_user_credentials.save()

        await delete_cached_user_credentials_async(redis_client, dto.temp_user_ulid)

        user_credentials = data_user_credentials_to_model(data_user_credentials)
        await set_cached_user_credentials_async(
            redis_client, dto.final_user_ulid, user_credentials
        )
