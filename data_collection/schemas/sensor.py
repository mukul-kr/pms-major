from pydantic import BaseModel, Field


class SensorBaseSchema(BaseModel):
    name: str = Field(alias="sn")
    value: float
    is_minimum_better: bool
    # user_id: str
    # project_id: str


class CreateSensorSchema(SensorBaseSchema):
    pass


class BaseSchema(SensorBaseSchema):
    class Config:
        orm_mode = True
