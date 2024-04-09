from sqlalchemy.orm import Session

from models.data import Data
from schemas.data import CreateDataSchema, DataRetrievalSchema
from models.device import Device
from typing import List

from datetime import datetime


def create_data(session: Session, data: CreateDataSchema):
    db_data = Data(**data.dict())
    session.add(db_data)
    session.commit()
    session.refresh(db_data)
    return db_data


def create_data_with_date_data(session: Session, data: DataRetrievalSchema):
    db_data = Data(**data.dict())
    session.add(db_data)
    session.commit()
    session.refresh(db_data)
    return db_data


def get_data_by_device_id(session: Session, device_id: int):
    return (
        session.query(Data)
        .filter(Data.device_id == device_id)
        .order_by(Data.created_at)
        .all()
    )


def get_data_by_sensor_id(session: Session, sensor_id: int):
    return (
        session.query(Data)
        .filter(Data.sensor_id == sensor_id)
        .order_by(Data.created_at)
        .all()
    )


def get_data_by_device_id_and_sensor_id(
    session: Session, device_id: int, sensor_id: int
):
    return (
        session.query(Data)
        .filter(Data.device_id == device_id, Data.sensor_id == sensor_id)
        .order_by(Data.created_at)
        .all()
    )


def get_data_by_device_id_and_sensor_id_and_timerange(
    session: Session,
    device_id: int,
    sensor_id: int,
    start_time: str,
    end_time: str,
):
    return (
        session.query(Data)
        .filter(
            Data.device_id == device_id,
            Data.sensor_id == sensor_id,
            Data.created_at >= start_time,
            Data.created_at <= end_time,
        )
        .order_by(Data.created_at)
        .all()
    )


def get_data_by_timerange(
    session: Session,
    start_time: str,
    end_time: str,
):
    return (
        session.query(Data)
        .filter(
            Data.created_at >= start_time,
            Data.created_at <= end_time,
        )
        .order_by(Data.created_at)
        .all()
    )


def get_data_by_device_id_and_timerange(
    session: Session,
    device_id: int,
    start_time: str,
    end_time: str,
):
    return (
        session.query(Data)
        .filter(
            Data.device_id == device_id,
            Data.created_at >= start_time,
            Data.created_at <= end_time,
        )
        .order_by(Data.created_at)
        .all()
    )


def get_data_of_multiple_device_multiple_sensor_by_timerange(
    session: Session,
    user_id: int,
    device_id_list: list,
    sensor_id_list: list,
    start_time: datetime,
    end_time: datetime,
) -> List[Data]:
    data = (
        session.query(Data)
        .join(Device)
        .filter(
            Device.user_id == user_id,
            Data.device_id.in_(device_id_list),
            Data.sensor_id.in_(sensor_id_list),
            Data.created_at >= start_time,
            Data.created_at <= end_time,
        )
        .order_by(Data.created_at)
        .all()
    )
    return data


def get_data_of_device_user_by_timerange(
    session: Session,
    user_id: int,
    start_time: datetime,
    end_time: datetime,
) -> List[Data]:
    data = (
        session.query(Data)
        .join(Device)
        .filter(
            Device.user_id == user_id,
            Data.created_at >= start_time,
            Data.created_at <= end_time,
        )
        .order_by(Data.created_at)
        .all()
    )
    return data
