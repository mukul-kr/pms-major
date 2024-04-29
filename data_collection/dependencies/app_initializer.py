from starlette.templating import Jinja2Templates
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session
from routes.v1.device.device import notify_inactive_device
from fastapi import Depends
from dependencies.db_initializer import get_db
from dependencies.http_initializer import dataClient
import os
from fastapi.middleware.cors import CORSMiddleware
from settings import INTERNAL_COMMUNICATION_SECRET

app = FastAPI()

templates = Jinja2Templates(
    directory=os.path.abspath(os.path.expanduser("templates"))
)


origins = [
    "http://pms-major-juet.netlify.app/",
    "https://pms-major-juet.netlify.app/",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
@repeat_every(seconds=6*60*60)  # 6 hours
async def periodic_task():
    # Your task here
    # ...
    print(1)
    print(
        dataClient.post_execute_device_off_check(
            {"secret": INTERNAL_COMMUNICATION_SECRET}
        )
    )
    # print(notify_inactive_device(session))
