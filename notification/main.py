from routes.v1.api import EmailApi, DocsApi

from dependencies.app_initializer import app

app.include_router(
    EmailApi.get_public_router(),
    prefix="/notification",
)

app.include_router(
    DocsApi.get_public_router(),
    prefix="/notification",
)
