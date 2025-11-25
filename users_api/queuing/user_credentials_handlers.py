from tortoise.transactions import in_transaction

from shared.event_models.user_credentials import UserCredentialsCreated
from shared.event_models.users import UserCreated
from shared.lib.redis_utils import get_redis_client
from users_api.data.entities.data_user import DataUser
from users_api.data.mapper_utils import data_user_to_model
from users_api.data.redis_query_utils import (
    delete_cached_user_async,
    set_cached_user_async,
)
from users_api.queuing.user_publisher import publish_user_created_async


async def handle_user_credentials_created_async(dto: UserCredentialsCreated):
    redis_client = get_redis_client()

    async with in_transaction():
        new_user = await DataUser.create()
        user = data_user_to_model(new_user)
        await set_cached_user_async(redis_client, new_user.ulid, user)

        try:
            await publish_user_created_async(
                UserCreated(
                    final_user_ulid=new_user.ulid, temp_user_ulid=dto.temp_user_ulid
                )
            )
        except Exception as e:
            await delete_cached_user_async(redis_client, new_user.ulid)
            raise e
