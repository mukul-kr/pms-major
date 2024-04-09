from pydantic import BaseModel, Field, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr
    area: str
    phone_number: str
    full_name: str


class CreateUserSchema(UserBaseSchema):
    hashed_password: str = Field(alias="password")


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(alias="username")
    password: str


class InternalUserSchema(BaseModel):
    id: int
    secret: str


class ValidateUserSchema(InternalUserSchema):
    ...


class UserNotificationSchema(InternalUserSchema):
    ...


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool = Field(default=False)

    class Config:
        orm_mode = True


class ValidationResponseSchema(BaseModel):
    user_id: int
    valid: bool
