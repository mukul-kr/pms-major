from models.device import Device
from data.sensor import (
    list_sensors_by_user_id,
    list_sensors_by_user_id_and_device_ids,
    list_sensors,
)


def query_sensor_handler(session, token, device_ids):
    decoded_token = Device.decode_token(token)
    user_id = decoded_token["sub"]
    if len(device_ids) == 0:
        return list_sensors_by_user_id(session=session, user_id=int(user_id))
    else:
        return list_sensors_by_user_id_and_device_ids(
            session=session, user_id=int(user_id), device_ids=device_ids
        )


def all_sensor_handler(session):
    return list_sensors(session=session)
