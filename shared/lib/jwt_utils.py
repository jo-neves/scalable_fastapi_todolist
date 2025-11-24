from datetime import timedelta

import jwt

from shared.lib.application_variables import ApplicationVariables
from shared.lib.constants import (
    DEFAULT_JWT_EXPIRE_MINUTES,
)
from shared.lib.date_utils import now_utc
from shared.models.jwt_dtos import JwtTokenData, JwtTokenDataInput


def create_access_token(
    jwt_token_data: JwtTokenDataInput, expires_delta: timedelta | None = None
):
    to_encode = jwt_token_data.model_dump()

    if expires_delta:
        expire = now_utc() + expires_delta
    else:
        expire = now_utc() + timedelta(minutes=DEFAULT_JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        ApplicationVariables.JWT_SECRET_KEY(),
        algorithm=ApplicationVariables.JWT_ALGORITHM(),
    )


def decode_token(token: str) -> JwtTokenData:
    payload = jwt.decode(
        token,
        ApplicationVariables.JWT_SECRET_KEY(),
        algorithms=[ApplicationVariables.JWT_ALGORITHM() or ""],
    )

    return JwtTokenData(**payload)


def is_user_jwt_admin(token: str):
    return decode_token(token=token).admin
