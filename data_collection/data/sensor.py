from sqlalchemy.orm import Session
from models.data import Data
from models.device import Device


from models.sensor import Sensor
from schemas.sensor import CreateSensorSchema


def create_sensor(session: Session, sensor: CreateSensorSchema):
    db_sensor = Sensor(**sensor.dict())
    session.add(db_sensor)
    session.commit()
    session.refresh(db_sensor)
    return db_sensor


def list_sensors(session: Session):
    return session.query(Sensor).all()


def get_sensor_by_name(session: Session, name: str):
    return session.query(Sensor).filter(Sensor.name == name).one()


def get_sensor_by_id(session: Session, id: int):
    return session.query(Sensor).filter(Sensor.id == id).one()


def update_sensor(session: Session, sensor: Sensor):
    session.add(sensor)
    session.commit()
    session.refresh(sensor)
    return sensor


def delete_sensor(session: Session, sensor: Sensor):
    session.delete(sensor)
    session.commit()
    return True


def delete_sensor_by_id(session: Session, id: int):
    session.query(Sensor).filter(Sensor.id == id).delete()
    session.commit()
    return True


def delete_sensor_by_name(session: Session, name: str):
    session.query(Sensor).filter(Sensor.name == name).delete()
    session.commit()
    return True


def get_sensor_by_device_id(session: Session, device_id: int):
    return session.query(Sensor).filter(Sensor.device_id == device_id).all()


def list_sensors_by_user_id(session: Session, user_id: int):
    # sensor doesn't have user_id. It is associated with device and device is associated with data
    # so we need to join the tables
    return (
        session.query(Sensor)
        .join(Data, Data.sensor_id == Sensor.id)
        .join(Device, Device.ext_id == Data.device_id)
        .filter(Device.user_id == user_id)
        .distinct()
        .all()
    )


def list_sensors_by_user_id_and_device_ids(
    session: Session, user_id: int, device_ids: list
):
    # sensor doesn't have user_id. It is associated with device and device is associated with data
    # so we need to join the tables
    return (
        session.query(Sensor)
        .join(Data, Data.sensor_id == Sensor.id)
        .join(Device, Device.ext_id == Data.device_id)
        .filter(Device.user_id == user_id, Device.id.in_(device_ids))
        .distinct()
        .all()
    )
