from json import dumps
from typing import Awaitable, Callable, Type, TypeVar

from aio_pika import ExchangeType, Message, connect_robust
from pydantic import BaseModel

from shared.lib.application_variables import ApplicationVariables


async def publish_to_topic_async(exchange_name: str, topic_name: str, dto: BaseModel):
    connection = await connect_robust(ApplicationVariables.RABBITMQ_URL())

    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange(exchange_name, ExchangeType.TOPIC)
        message = Message(body=dumps(dto).encode())

        await exchange.publish(message, routing_key=topic_name)


TMessage = TypeVar("TMessage", bound=BaseModel)
AsyncHandler = Callable[[TMessage], Awaitable[None]]


async def consume_topic_async(
    exchange_name: str,
    topic_name: str,
    queue_name: str,
    model_type: Type[TMessage],
    async_handler: AsyncHandler,
):
    """
    Example Usage: `select_distinct(exchange_name, topic_name, queue_name, ModelType, async_handler)`

    Args:
        exchange_name (str)
        topic_name (str)
        queue_name (str)
        model_type (Type[TMessage])
        async_handler (Callable[[TMessage], Awaitable[None]])
    """
    connection = await connect_robust(ApplicationVariables.RABBITMQ_URL())

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        await queue.bind(exchange_name, routing_key=topic_name)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await async_handler(model_type.model_validate_json(message.body))
