from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import tortoise_exception_handlers

from auth_api.queuing.user_handlers import handle_user_created_async
from routers.auth import api_auth_router
from shared.lib.constants import APP_NAME_AUTH_API
from shared.lib.fastapi_utils import app_add_cors, app_lifespan
from shared.queue_consumers.user_consumers import consume_user_created_async


async def app_on_init_async(_: FastAPI):
    await consume_user_created_async(
        app_name=APP_NAME_AUTH_API, async_handler=handle_user_created_async
    )


load_dotenv()

app = FastAPI(
    lifespan=app_lifespan(
        app_folder="auth_api",
        modules={
            "entities": [
                f"{APP_NAME_AUTH_API}.data.entities.data_user_credentials",
            ]
        },
        use_redis=True,
        additional_app_on_init_async=app_on_init_async,
    ),
    exception_handlers=tortoise_exception_handlers(),
)
app_add_cors(app)
app.include_router(api_auth_router, prefix="/api/v1")
