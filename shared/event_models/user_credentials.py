from pydantic import BaseModel
from shared.lib.types import UlidStr


class UserCredentialsCreated(BaseModel):
    temp_user_ulid: UlidStr
