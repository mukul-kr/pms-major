from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    UniqueConstraint,
    PrimaryKeyConstraint,
    ForeignKey,
)

from dependencies.db_initializer import Base

import bcrypt
import jwt
import settings


class Device(Base):
    """Models a Device table"""

    __tablename__ = "dc_device"
    ext_id = Column(String(225), nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    hashed_password = Column(LargeBinary, nullable=False)
    # user_id = Column(
    #     Integer,
    #     ForeignKey("users.id", ondelete="CASCADE"),
    #     nullable=False,
    # )
    # user = relationship('User', backref='devices')
    # user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'))
    # user = relationship('User', backref='devices')

    # Define the relationship with the User table
    user_id = Column(Integer, nullable=False)

    UniqueConstraint("ext_id", name="uq_device_ext_id")
    PrimaryKeyConstraint("id", name="pk_device_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {ext_id!r}>".format(ext_id=self.ext_id)

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

    # def generate_token(self) -> dict:
    # 	"""Generate access token for user"""
    # 	return {
    # 		"access_token": jwt.encode(
    # 			{
    #         "sub": self.id,
    #         "full_name": self.full_name,
    #         "email": self.email,
    #         "exp": datetime.utcnow() + timedelta(minutes=30)
    #     },
    # 			settings.SECRET_KEY
    # 		)
    # 	}

    @staticmethod
    def decode_token(token) -> dict:
        """Decode access token"""
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
