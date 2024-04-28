from data.device import get_device_by_ext_id, get_devices_with_data
from data.sensor import get_sensor_by_id
from domain.usecase.notify_inactive_devices import deviceEmailSchemaGenerator
from models.device import Device
from models.sensor import Sensor
from schemas.data import CreateDataSchema
from settings import INTERNAL_COMMUNICATION_SECRET
from sqlalchemy.orm import Session
from dependencies.http_initializer import authClient, notificationClient
from fastapi import HTTPException
from starlette import status


def checkHighSeverityDataNotify(session: Session, ext_device_id: str, sensor_id: int, value: int):
    try:
        device : Device = get_device_by_ext_id(session=session, ext_id=ext_device_id)
        sensor: Sensor = get_sensor_by_id(session=session, id=sensor_id)
        if not((sensor.alertDirection == 1 and value < sensor.value) or (sensor.alertDirection == 0 and value < sensor.lowerValueRange and value > sensor.upperValueRange) or (sensor.alertDirection == -1 and value > sensor.value)): # type: ignore
            return "Data is normal"
        
        payload = deviceEmailSchemaGenerator(device.user_id)
        response = authClient.post_get_user_by_id(payload=payload)
        print(response.json())
        payload = highSeverityNotificationSchemaGenerator(
            response.json()["email"],
            response.json()["full_name"],
            device.ext_id,  # type: ignore
            sensor.name,
            int(data.value),
        )
        response = notificationClient.post_high_severity_data_notification(payload=payload)

        return response.json()
            # return payload
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")

    return "All devices are active"
def highSeverityNotificationSchemaGenerator(
    email: str, name: str, device: str, sensor_name: str, value: int
):
    return {
        "email": email,
        "name": name,
        "event": "DataWarning",
        "secret": "myinternalcommunicationsecret",
        "additionalProp1": {
            "severity": "high",
            "device": device,
            "sensor": sensor_name,
            "value": value,
        },
    }
