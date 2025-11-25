from shared.event_models.user_credentials import UserCredentialsCreated
from shared.lib.constants import (
    EXCHANGE_USER_CREDENTIALS,
    TOPIC_USER_CREDENTIALS_CREATED,
)
from shared.lib.rabbitmq_utils import publish_to_topic_async


async def publish_user_credentials_created_async(dto: UserCredentialsCreated):
    await publish_to_topic_async(
        exchange_name=EXCHANGE_USER_CREDENTIALS,
        topic_name=TOPIC_USER_CREDENTIALS_CREATED,
        dto=dto,
    )
