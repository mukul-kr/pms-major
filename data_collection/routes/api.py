from abc import ABC, abstractmethod

from fastapi import APIRouter  # type: ignore


class APIRouter(ABC):
    def __init__(self, public_router: APIRouter, private_router: APIRouter):
        self.public_router = public_router
        self.private_router = private_router

        @self.public_router.get("/health-check")  # type: ignore
        def health_check():
            return {"status": "ok"}

    @abstractmethod
    def get_public_router():
        pass

    @abstractmethod
    def get_private_router():
        pass
