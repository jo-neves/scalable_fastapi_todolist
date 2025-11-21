from auth_api.data.entities.data_user_credentials import DataUserCredentials
from shared.models.auth_dtos import UserCredentials


def data_user_credentials_to_model(
    data_user_credentials: DataUserCredentials,
):
    return UserCredentials(
        user_ulid=data_user_credentials.user_ulid,
        email=data_user_credentials.email,
    )
