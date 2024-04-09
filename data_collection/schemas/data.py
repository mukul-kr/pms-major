from pydantic import BaseModel, Field


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


class DataBaseSchema(BaseModel):
    value: float
    sensor_id: int
    device_id: str = Field(alias="ext_id")


class CreateDataSchema(DataBaseSchema):
    hashed_password: str = Field(alias="p")


class BaseSchema(DataBaseSchema):
    class Config:
        orm_mode = True


class DataRetrievalSchema(DataBaseSchema):
    created_at: str


class DataQuerySchema(BaseModel):
    user_id: int
    start_date: str
    end_date: str
    device_id: str
    sensor_id: int
