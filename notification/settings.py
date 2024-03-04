import os

# import cloudinary

# Database url configuration

from dotenv import load_dotenv

load_dotenv()

REDIS_CONFIG = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": os.getenv("REDIS_PORT", 6379),
    "db": os.getenv("REDIS_DB", 0),
}

SECRET_KEY = os.getenv("SECRET_KEY")

INTERNAL_COMMUNICATION_SECRET = os.getenv("INTERNAL_COMMUNICATION_SECRET")


MAIL_PORT = os.getenv("MAIL_PORT", "465")
MAIL_SMTP_SERVER = os.getenv("MAIL_SMTP_SERVER", "smtp.gmail.com")
EMAIL = os.getenv("EMAIL", "mukul0000kumar@gmail.com")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD", "nwwbrjbummdmncey")
