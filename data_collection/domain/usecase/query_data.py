from data.data import (
    get_data_of_multiple_device_multiple_sensor_by_timerange,
    get_data_of_device_user_by_timerange,
)
from models.device import Device


def query_data_handler(
    session, start_date, end_date, device_id, sensor_id, token
):
    decoded_token = Device.decode_token(token)
    user_id = decoded_token["sub"]
    if len(device_id) == 0 and len(sensor_id) == 0:
        return get_data_of_device_user_by_timerange(
            session=session,
            user_id=user_id,
            start_time=start_date,
            end_time=end_date,
        )
    else:
        return get_data_of_multiple_device_multiple_sensor_by_timerange(
            session=session,
            user_id=user_id,
            device_id_list=device_id,
            sensor_id_list=sensor_id,
            start_time=start_date,
            end_time=end_date,
        )
