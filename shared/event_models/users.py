from pydantic import BaseModel

from shared.lib.types import UlidStr


class UserCreated(BaseModel):
    final_user_ulid: UlidStr
    temp_user_ulid: UlidStr
