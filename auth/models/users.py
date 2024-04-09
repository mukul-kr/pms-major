from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    PrimaryKeyConstraint,
)

import jwt
import bcrypt

from dependencies.db_initializer import Base

import settings
from datetime import datetime, timedelta


class User(Base):
    """Models a user table"""

    __tablename__ = "users"
    email = Column(String(225), nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    hashed_password = Column(LargeBinary, nullable=False)
    full_name = Column(String(225), nullable=False)
    area = Column(String(225), nullable=True)
    phone_number = Column(String(16), nullable=False)
    is_active = Column(Boolean, default=False)

    UniqueConstraint("email", name="uq_user_email")
    UniqueConstraint("phone_number", name="uq_user_phone_number")
    PrimaryKeyConstraint("id", name="pk_user_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {full_name!r}>".format(full_name=self.full_name)

    @staticmethod
    def hash_password(password) -> bytes:
        """Transforms password from it's raw textual form to
        cryptographic hashes
        """
        return bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        )  # .decode()

    def validate_password(self, password) -> bool:
        """Confirms password validity"""
        return bcrypt.checkpw(password.encode("utf-8"), self.hashed_password)  # type: ignore

    def generate_token(self) -> dict:
        """Generate access token for user"""
        return {
            "access_token": jwt.encode(
                {
                    "sub": self.id,
                    "full_name": self.full_name,
                    "email": self.email,
                    "exp": datetime.utcnow() + timedelta(days=30),
                },
                settings.SECRET_KEY,
            ),
            "username": self.full_name,
        }

    @staticmethod
    def decode_token(token) -> dict:
        """Decode access token"""
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
