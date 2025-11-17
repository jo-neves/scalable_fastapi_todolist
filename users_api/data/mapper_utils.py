from shared.models.user_dto import User
from users_api.data.entities.data_user import DataUser


def data_user_to_model(data_user: DataUser):
    return User(
        ulid=data_user.ulid,
        first_name=data_user.first_name,
        last_name=data_user.last_name,
        credentials=None,
    )


def update_data_user_from_model(data_user: DataUser, user: User):
    data_user.first_name = user.first_name or ""
    data_user.last_name = user.last_name or ""
