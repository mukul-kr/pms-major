import os

# import cloudinary

# Database url configuration

from dotenv import load_dotenv


import pytz

load_dotenv()

_prefix = "postgresql+psycopg2://"

DATABASE_URL = "{_prefix}{username}:{password}@{host}:{port}/{db_name}".format(
    _prefix=_prefix,
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    db_name=os.getenv("POSTGRES_DB"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

REDIS_CONFIG = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": os.getenv("REDIS_PORT", 6379),
    "db": os.getenv("REDIS_DB", 0),
}

SECRET_KEY = os.getenv("SECRET_KEY")

INTERNAL_COMMUNICATION_SECRET = os.getenv(
    "INTERNAL_COMMUNICATION_SECRET", "string"
)

INTERNAL_COMMUNICATION_URL = os.getenv(
    "INTERNAL_COMMUNICATION_URL", "http://localhost:8000"
)


IST_TIMEZONE = pytz.timezone("Asia/Kolkata")
