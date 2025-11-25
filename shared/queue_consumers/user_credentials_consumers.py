from shared.event_models.user_credentials import UserCredentialsCreated
from shared.lib.constants import (
    EXCHANGE_USER_CREDENTIALS,
    TOPIC_USER_CREDENTIALS_CREATED,
)
from shared.lib.rabbitmq_utils import AsyncHandler, consume_topic_async


async def consume_user_credentials_created_async(app_name: str, async_handler: AsyncHandler):
    await consume_topic_async(
        exchange_name=EXCHANGE_USER_CREDENTIALS,
        topic_name=TOPIC_USER_CREDENTIALS_CREATED,
        queue_name=f"user_credentials_created_queue__{app_name}",
        model_type=UserCredentialsCreated,
        async_handler=async_handler,
    )
