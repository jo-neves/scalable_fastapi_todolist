from tortoise import Model, fields

from shared.lib.tortoise_utils import ulid_field


class DataUser(Model):
    id = fields.IntField(primary_key=True)
    ulid = ulid_field()
    first_name = fields.CharField(max_length=20, null=True)
    last_name = fields.CharField(max_length=20, null=True)
    profile_picture = fields.CharField(max_length=2000, null=True)

    # credentials: fields.OneToOneRelation[DataUserCredentials] | None = (
    #     fields.OneToOneField(
    #         "entities.DataUserCredentials",
    #         on_delete=fields.CASCADE,
    #         null=True,
    #         default=None,
    #         lazy=False,
    #     )
    # )

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
