from data.device import create_device
from exception.device import InvalidUserIdException
from domain.usecase.validate_user import validate_user
from models.device import Device


def create_device_handler(session, payload):
    # verify payload.user_id
    if (
        payload.user_id is None
        or payload.user_id == ""
        or not does_user_exists(payload.user_id)
    ):
        raise InvalidUserIdException("Invalid user id")
    # payload.hashed_password = Device.hash_password(payload.hashed_password)
    return create_device(session, device=payload)


def does_user_exists(user_id: int) -> bool:
    # verify user_id
    return validate_user(user_id=user_id)
