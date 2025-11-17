from typing import Annotated

from pydantic import AfterValidator, BaseModel

from shared.lib.ulid_validators import validate_str_ulid
from shared.models.auth_dtos import UserCredentials


class User(BaseModel):
    ulid: Annotated[str, AfterValidator(validate_str_ulid)]
    first_name: str | None
    last_name: str | None
    credentials: UserCredentials | None
