from pydantic import BaseModel

from shared.lib.types import UlidStr


class NewItem(BaseModel):
    user_ulid: UlidStr
    title: str
    description: str
    done: bool = False


class Item(NewItem):
    ulid: UlidStr
