from shared.event_models.users import UserCreated
from shared.lib.constants import (
    EXCHANGE_USERS,
    TOPIC_USER_CREATED,
)
from shared.lib.rabbitmq_utils import AsyncHandler, consume_topic_async


async def consume_user_created_async(app_name: str, async_handler: AsyncHandler):
    await consume_topic_async(
        exchange_name=EXCHANGE_USERS,
        topic_name=TOPIC_USER_CREATED,
        queue_name=f"user_created_queue__{app_name}",
        model_type=UserCreated,
        async_handler=async_handler,
    )
