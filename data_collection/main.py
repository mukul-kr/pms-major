from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session
from domain.usecase.notify_inactive_devices import notify_inactive_devices
from dependencies.db_initializer import get_db


import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from dependencies.app_initializer import app

from routes.v1.api import (
    device_collection_api,
    data_collection_api,
    sensor_collection_api,
    docs_api,
)

app.include_router(
    device_collection_api.get_public_router(), prefix="/api"  # type: ignore
)

app.include_router(
    device_collection_api.get_private_router(), prefix="/api"  # type: ignore
)

app.include_router(
    sensor_collection_api.get_public_router(), prefix="/api"  # type: ignore
)

app.include_router(
    sensor_collection_api.get_private_router(), prefix="/api"  # type: ignore
)


app.include_router(
    data_collection_api.get_public_router(), prefix="/api"  # type: ignore
)

app.include_router(
    data_collection_api.get_private_router(), prefix="/api"  # type: ignore
)


app.include_router(docs_api.get_public_router(), prefix="/api")  # type: ignore
