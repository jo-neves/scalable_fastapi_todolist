from tortoise import fields

from shared.lib.ulid_utils import new_ulid_str


def ulid_field(unique: bool = True, index: bool = True):
    return fields.CharField(
        default=new_ulid_str, max_length=27, unique=unique, index=index
    )
