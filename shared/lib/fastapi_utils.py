import os
from contextlib import asynccontextmanager
from types import ModuleType
from typing import Iterable

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import RegisterTortoise

from shared.lib.application_variables import ApplicationVariables
from shared.lib.constants import INTERNAL_API_KEY_HEADER_NAME
from shared.lib.fs_utils import working_dir_endswith
from shared.lib.redis_utils import _redis_client, close_redis_async, init_redis_client


def app_lifespan(
    app_folder: str,
    modules: dict[str, Iterable[str | ModuleType]] | None,
    db_url: str | None = None,
    use_redis: bool = False,
):
    @asynccontextmanager
    async def lifespan_async(app: FastAPI):
        # Different environments have different working directories.
        # Docker doesn't need the app_folder, only in local mode.
        needed_app_folder = "" if working_dir_endswith(app_folder) else app_folder

        if use_redis:
            init_redis_client(ApplicationVariables.REDIS_HOST() or "127.0.0.1", 6379)

        async with RegisterTortoise(
            app=app,
            modules=modules,
            db_url=db_url
            or f"sqlite:///{os.path.abspath(os.path.join(needed_app_folder, 'data', 'db', 'db.sqlite3'))}",
            # Use UTC.
            use_tz=True,
            add_exception_handlers=True,
            generate_schemas=True,
        ):
            yield
            if use_redis:
                await close_redis_async()

    return lifespan_async


def app_add_cors(app: FastAPI):
    origins = [
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8001",
        "http://127.0.0.1:8002",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def request_is_internal_api_key_valid(request: Request):
    internal_api_key = request.headers.get(INTERNAL_API_KEY_HEADER_NAME)
    return internal_api_key == ApplicationVariables.INTERNAL_API_KEY()
