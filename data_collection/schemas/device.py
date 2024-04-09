from pydantic import BaseModel, Field


class DeviceBaseSchema(BaseModel):
    ext_id: str = Field(alias="ext")
    user_id: int = Field(alias="u")


class CreateDeviceSchema(DeviceBaseSchema):
    hashed_password: str = Field(alias="p")


class BaseSchema(DeviceBaseSchema):
    class Config:
        orm_mode = True


class ValidateSchema(BaseModel):
    secret: str
