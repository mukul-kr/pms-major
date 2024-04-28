from pydantic import BaseModel, Field


class SensorBaseSchema(BaseModel):
    name: str = Field(alias="sn")
    value: float
    alertDirection: int
    upperValueRange: float
    lowerValueRange: float



class CreateSensorSchema(SensorBaseSchema):
    pass


class BaseSchema(SensorBaseSchema):
    class Config:
        orm_mode = True
