from routes.v1.data.data import (
    public_router as data_pub_ro,
    private_router as data_pri_ro,
)
from routes.v1.device.device import (
    public_router as device_pub_ro,
    private_router as device_pri_ro,
)
from routes.v1.sensor.sensor import (
    public_router as sensor_pub_ro,
    private_router as sensor_pri_ro,
)

from routes.v1.generic.docs import (
    public_router as docs_pub_ro,
)

from fastapi import APIRouter

from routes.api import APIRouter


class DataCollectionApi(APIRouter):
    def __init__(self, public_router, private_router):
        super().__init__(public_router, private_router)

    def get_public_router(self):
        return self.public_router

    def get_private_router(self):
        return self.private_router


class DeviceCollectionApi(APIRouter):
    def __init__(self, public_router, private_router):
        super().__init__(public_router, private_router)

    def get_public_router(self):
        return self.public_router

    def get_private_router(self):
        return self.private_router


class SensorCollectionApi(APIRouter):
    def __init__(self, public_router, private_router):
        super().__init__(public_router, private_router)

    def get_public_router(self):
        return self.public_router

    def get_private_router(self):
        return self.private_router


class DocsApi(APIRouter):
    def __init__(self, public_router):
        super().__init__(public_router, public_router)

    def get_public_router(self):
        return self.public_router

    def get_private_router(self):
        return


data_collection_api = DataCollectionApi(data_pub_ro, data_pri_ro)  # type: ignore
device_collection_api = DeviceCollectionApi(device_pub_ro, device_pri_ro)  # type: ignore
sensor_collection_api = SensorCollectionApi(sensor_pub_ro, sensor_pri_ro)  # type: ignore
docs_api = DocsApi(docs_pub_ro)  # type: ignore
