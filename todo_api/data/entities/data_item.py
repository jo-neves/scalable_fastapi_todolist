from tortoise import Model, fields

from shared.lib.tortoise_utils import ulid_field


class DataItem(Model):
    id = fields.IntField(primary_key=True)
    ulid = ulid_field()
    user_ulid = ulid_field()

    # user: fields.ForeignKeyRelation[DataUser] = fields.ForeignKeyField(
    #     "entities.DataUser",
    #     related_name="DataItem",
    #     on_delete=fields.OnDelete.CASCADE,
    # )

    title = fields.CharField(max_length=50)
    description = fields.CharField(max_length=200)
    done = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
