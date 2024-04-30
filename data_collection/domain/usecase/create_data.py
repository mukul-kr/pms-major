from data.data import create_data, create_data_with_date_data

from domain.usecase.alert_high_data import checkHighSeverityDataNotify
from domain.usecase.query_data import get_latest_device_sensor_handler
from schemas.data import DataBaseSchema
from dependencies.model import predict

def create_data_handler(session, payload):
    if not validate_sensor(payload.sensor_id):
        raise Exception("Invalid sensor id")
    if not validate_device(payload.device_id):
        raise Exception("Invalid device id")

    checkHighSeverityDataNotify(session, payload.device_id, payload.sensor_id, payload.value)    

    if payload.sensor_id == 4:
        tds_data = get_latest_device_sensor_handler(session, payload.device_id, 1)
        ph_data = get_latest_device_sensor_handler(session, payload.device_id, 2)
        trubidity_data = get_latest_device_sensor_handler(session, payload.device_id, 3)
        new_payload = DataBaseSchema(
            value=min(0,max(predict([[tds_data.value, ph_data.value, trubidity_data.value]]), 1)),
            sensor_id=payload.sensor_id,
            ext_id=payload.device_id,
        )
    else:
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
