from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.data import Data
from models.device import Device
from schemas.device import CreateDeviceSchema
from exception import device as device_exception


def create_device(session: Session, device: CreateDeviceSchema):
    db_device = Device(**device.dict())
    session.add(db_device)
    session.commit()
    session.refresh(db_device)
    return db_device


def get_device_by_ext_id(session: Session, ext_id: str):
    return session.query(Device).filter(Device.ext_id == ext_id).one()


def validate_device(session: Session, ext_id: str, password: str):
    try:
        device: Device = get_device_by_ext_id(session=session, ext_id=ext_id)
    except Exception as e:
        raise device_exception.DeviceNotFoundException(f"Device not found {e}")

    is_validated: bool = device.validate_password(password=password)
    if not is_validated:
        raise device_exception.DeviceCredentialNotMatchedException(
            "Invalid password"
        )


def get_device_by_id(session: Session, id: int):
    return session.query(Device).filter(Device.id == id).one()


def update_device(session: Session, device: Device):
    session.add(device)
    session.commit()
    session.refresh(device)
    return device


def delete_device(session: Session, device: Device):
    session.delete(device)
    session.commit()
    return True


def delete_device_by_id(session: Session, id: int):
    session.query(Device).filter(Device.id == id).delete()
    session.commit()
    return True


def delete_device_by_ext_id(session: Session, ext_id: str):
    session.query(Device).filter(Device.ext_id == ext_id).delete()
    session.commit()
    return True


# list devices by user id
def list_devices_by_user_id(session: Session, user_id: int):
    return session.query(Device).filter(Device.user_id == user_id).all()


def get_devices_with_data(session):
    current_time = datetime.utcnow()
    twentyfour_hours_ago = current_time - timedelta(hours=24)
    thirty_minutes_ago = current_time - timedelta(minutes=30)

    devices_with_data = (
        session.query(Device)
        .join(Data)
        .filter(
            Data.created_at >= twentyfour_hours_ago,
            Data.created_at <= current_time,
        )
        .filter(~Data.created_at.between(thirty_minutes_ago, current_time))
        .distinct()
        .all()
    )

    return devices_with_data
