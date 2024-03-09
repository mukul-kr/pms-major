from routes.v1.email.email import (
    public_router as auth_public_router,
)

from routes.v1.generic.docs import public_router as docs_public_router
from routes.api import APIRouter

# from routes.v1.generic.docs import public_router as docs_public_router


class EmailApi(APIRouter):
    public_router = auth_public_router

    @staticmethod
    def get_public_router():
        return auth_public_router


class DocsApi(APIRouter):
    public_router = docs_public_router

    @staticmethod
    def get_public_router():
        return docs_public_router
