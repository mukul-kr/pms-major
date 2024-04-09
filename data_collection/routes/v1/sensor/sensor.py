from . import get_private_router, get_public_router

from fastapi import Depends, Body, Query
from dependencies.db_initializer import get_db
from sqlalchemy.orm import Session
from domain.usecase.create_sensor import create_sensor_handler
from schemas.sensor import CreateSensorSchema
from domain.usecase.query_sensor import (
    query_sensor_handler,
    all_sensor_handler,
)
from domain.usecase.validation import TokenValidation
from typing import List

public_router = get_public_router()
private_router = get_private_router()


@private_router.post("/sensor")
def create_sensor(
    payload: CreateSensorSchema = Body(), session: Session = Depends(get_db)
):
    return create_sensor_handler(session=session, payload=payload)


@private_router.get("/sensor")
def get_sensor(
    token: str = Depends(TokenValidation.is_token_invalid),
    session: Session = Depends(get_db),
    device_ids: List[str] = Query(
        default=[], description="Comma-separated list of device IDs"
    ),
):
    return query_sensor_handler(
        session=session, token=token, device_ids=device_ids
    )


@private_router.get("/all-sensor")
def get_all_sensor(
    session: Session = Depends(get_db),
):
    return all_sensor_handler(session)
