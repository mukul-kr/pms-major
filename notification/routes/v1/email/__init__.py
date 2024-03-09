from fastapi import APIRouter


def get_public_router():
    router = APIRouter()
    # router.prefix = "/"
    router.tags = ["public"]
    return router
