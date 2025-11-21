from tortoise import Model, fields

from shared.lib.tortoise_utils import ulid_field


class DataUserCredentials(Model):
    id = fields.IntField(primary_key=True)
    user_ulid = ulid_field()
    email = fields.CharField(max_length=150, unique=True)
    password_hash = fields.CharField(max_length=150)
    salt = fields.CharField(max_length=150, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
