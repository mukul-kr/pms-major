from routes.v1.api import DocsApi, UserApi

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

from dependencies.app_initializer import app

app.include_router(
    UserApi.get_public_router(),
    prefix="/auth",
)

app.include_router(
    UserApi.get_private_router(),
    prefix="/auth",
)

app.include_router(
    DocsApi.get_public_router(),
)
