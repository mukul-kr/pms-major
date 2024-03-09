from pydantic import BaseModel, ConfigDict, EmailStr, Extra


class EmailSchema(BaseModel):
    email: EmailStr
    name: str
    event: str
    secret: str
    model_config = ConfigDict(extra="allow")
    # class Config:
    #     extra = Extra.allow
    #     extra_kwargs = {"device": {"required": False}}


class EmailResponseSchema(BaseModel):
    status: str
