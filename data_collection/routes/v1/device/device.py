from . import get_private_router, get_public_router
from schemas.device import CreateDeviceSchema, ValidateSchema
from sqlalchemy.orm import Session

from fastapi import status, HTTPException, Depends, Body
from dependencies.db_initializer import get_db

from domain.usecase.create_device import create_device_handler
from domain.usecase.query_device import query_device_handler
from domain.usecase.validation import (
    TokenValidation,
    isInternalCommunicationChannelVerified,
)
from domain.usecase.notify_inactive_devices import notify_inactive_devices

public_router = get_public_router()
private_router = get_private_router()


@private_router.post("/device")
def create_device(
    payload: CreateDeviceSchema = Body(), session: Session = Depends(get_db)
):
    try:
        return create_device_handler(session, payload=payload)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@private_router.get("/device")
def get_device(
    token: str = Depends(TokenValidation.is_token_invalid),
    session: Session = Depends(get_db),
):
    return query_device_handler(session=session, token=token)


@public_router.post("/notify-dead-device")
def notify_inactive_device(
    session: Session = Depends(get_db), payload: ValidateSchema = Body()
):
    try:
        isInternalCommunicationChannelVerified(secret=payload.secret)
        return notify_inactive_devices(session=session)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
