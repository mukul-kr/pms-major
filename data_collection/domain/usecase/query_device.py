from models.device import Device

from data.device import list_devices_by_user_id


def query_device_handler(session, token):
    decoded_token = Device.decode_token(token)
    user_id = decoded_token["sub"]

    return list_devices_by_user_id(session=session, user_id=int(user_id))
