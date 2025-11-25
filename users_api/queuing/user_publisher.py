from shared.event_models.users import UserCreated
from shared.lib.constants import EXCHANGE_USERS, TOPIC_USER_CREATED
from shared.lib.rabbitmq_utils import publish_to_topic_async


async def publish_user_created_async(dto: UserCreated):
    await publish_to_topic_async(
        exchange_name=EXCHANGE_USERS,
        topic_name=TOPIC_USER_CREATED,
        dto=dto,
    )
