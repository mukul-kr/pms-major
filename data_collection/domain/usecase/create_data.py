from data.data import create_data, create_data_with_date_data

from schemas.data import DataBaseSchema


def create_data_handler(session, payload):
    if not validate_sensor(payload.sensor_id):
        raise Exception("Invalid sensor id")
    if not validate_device(payload.device_id):
        raise Exception("Invalid device id")
    new_payload = DataBaseSchema(
        value=payload.value,
        sensor_id=payload.sensor_id,
        ext_id=payload.device_id,
    )

    return create_data(session, new_payload)  # type: ignore


def validate_sensor(sensor_id: int) -> bool:
    # verify sensor_id
    return True


def validate_device(device_id: str) -> bool:
    # verify device_id
    return True


def create_data_with_date_without_verification_handler(session, payload):
    return create_data_with_date_data(session, payload)
