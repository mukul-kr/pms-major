from data.device import get_devices_with_data
from settings import INTERNAL_COMMUNICATION_SECRET
from sqlalchemy.orm import Session
from dependencies.http_initializer import authClient, notificationClient
from fastapi import HTTPException
from starlette import status


def notify_inactive_devices(session: Session):
    try:
        devices = get_devices_with_data(session=session)
        print(devices)
        for device in devices:
            print(device)
            user_id = int(device.user_id)  # type: ignore
            payload = deviceEmailSchemaGenerator(user_id)
            response = authClient.post_get_user_by_id(payload=payload)
            print(response.json())
            payload = notificationSchemaGenerator(
                response.json()["email"],
                response.json()["full_name"],
                device.ext_id,  # type: ignore
            )
            print(payload)
            response = notificationClient.post_device_off_notification(
                payload=payload
            )

            return response.json()
            # return payload
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}"
        )

    return "All devices are active"


def deviceEmailSchemaGenerator(user_id: int):
    return {"id": user_id, "secret": INTERNAL_COMMUNICATION_SECRET}


def notificationSchemaGenerator(email: str, name: str, device: str):
    return {
        "email": email,
        "name": name,
        "event": "DeviceStopped",
        "secret": "myinternalcommunicationsecret",
        "additionalProp1": {"device": device},
    }
