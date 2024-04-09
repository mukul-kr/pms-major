from . import get_private_router, get_public_router

from fastapi import Depends, Body, Query
from dependencies.db_initializer import get_db
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List
from schemas.data import CreateDataSchema, DataRetrievalSchema
from domain.usecase.validation import TokenValidation

from domain.usecase.create_data import (
    create_data_handler,
    create_data_with_date_without_verification_handler,
)
from domain.usecase.query_data import query_data_handler

from settings import IST_TIMEZONE

public_router = get_public_router()
private_router = get_private_router()


@public_router.post("/data")
def create_data(
    payload: CreateDataSchema = Body(), session: Session = Depends(get_db)
):
    return create_data_handler(session=session, payload=payload)


@private_router.get("/data")
def get_data(
    start_date: datetime = Query(
        default=datetime.now(tz=IST_TIMEZONE) - timedelta(days=1),
        description="Start date in ISO 8601 format",
    ),
    end_date: datetime = Query(
        default=datetime.now(tz=IST_TIMEZONE),
        description="End date in ISO 8601 format",
    ),
    device_ids: List[str] = Query(
        default=[], description="Comma-separated list of device IDs"
    ),
    sensor_ids: List[int] = Query(
        default=[], description="Comma-separated list of sensor IDs"
    ),
    session: Session = Depends(get_db),
    token: str = Depends(TokenValidation.is_token_invalid),
):
    data = query_data_handler(
        start_date=start_date,
        end_date=end_date,
        device_id=device_ids,
        sensor_id=sensor_ids,
        session=session,
        token=token,
    )
    return data


@public_router.post("/data-with-date")
def create_data_with_date(
    payload: DataRetrievalSchema = Body(), session: Session = Depends(get_db)
):
    return create_data_with_date_without_verification_handler(
        session=session, payload=payload
    )
