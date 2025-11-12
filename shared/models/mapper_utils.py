from auth_api.data.entities.data_user_credentials import DataUserCredentials
from shared.models.auth_dtos import UserCredentials
from shared.models.user_dto import User
from shared.models.items_dtos import Item, NewItem
from todo_api.data.entities.data_item import DataItem
from users_api.data.entities.data_user import DataUser


def data_user_to_model(data_user: DataUser):
    return User(
        ulid=data_user.ulid,
        first_name=data_user.first_name,
        last_name=data_user.last_name,
        credentials=None,
    )


def data_user_credentials_to_model(
    data_user_credentials: DataUserCredentials,
):
    return UserCredentials(
        user_ulid=data_user_credentials.user_ulid,
        email=data_user_credentials.email,
    )


def update_data_user_from_model(data_user: DataUser, user: User):
    data_user.first_name = user.first_name or ""
    data_user.last_name = user.last_name or ""


def update_data_item_from_model(data_item: DataItem, item: Item | NewItem) -> DataItem:
    data_item.user_ulid = item.user_ulid
    data_item.title = item.title
    data_item.description = item.description
    data_item.done = item.done

    return data_item


def data_item_to_model(data_item: DataItem):
    return Item(
        ulid=data_item.ulid,
        user_ulid=data_item.user_ulid,
        title=data_item.title,
        description=data_item.description,
        done=data_item.done,
    )
