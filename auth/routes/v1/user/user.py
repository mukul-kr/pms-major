from exception.user import CommunicationChannelNotVerifiedException
from . import get_private_router, get_public_router

from typing import Dict

from fastapi import HTTPException, Depends, Body, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from domain.usecase.validation import isUserValid

from domain.usecase import (
    login as login_usecase,
    signup as signup_usecase,
    profile as profile_usecase,
    logout as logout_usecase,
    validation as validation_usecase,
)
from dependencies.db_initializer import get_db, oauth2_scheme

from schemas.users import (
    CreateUserSchema,
    InternalUserSchema,
    UserSchema,
    ValidateUserSchema,
    ValidationResponseSchema,
)

public_router = get_public_router()
private_router = get_private_router()


@public_router.post("/login", response_model=Dict)
def login(
    payload: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db),
):
    try:
        user = login_usecase.login_handler(
            session=session,
            username=payload.username,
            password=payload.password,
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

    return user.generate_token()


@public_router.post("/signup", response_model=UserSchema)
def signup(
    background_tasks: BackgroundTasks,
    payload: CreateUserSchema = Body(),
    session: Session = Depends(get_db),
):
    try:
        user = signup_usecase.signup_handler(
            payload=payload, session=session, background_tasks=background_tasks
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


# modify this so that it gives current user details.
@private_router.get("/profile", response_model=UserSchema)
def profile(
    session: Session = Depends(get_db),
    token: str = Depends(validation_usecase.TokenValidation.is_token_invalid),
):
    try:
        return profile_usecase.getSignedInUserDetail(
            token=token, session=session
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@public_router.post("/validate-user", response_model=ValidationResponseSchema)
def validate_user(
    payload: ValidateUserSchema = Body(),
    session: Session = Depends(get_db),
):
    # Implement logic to check if the user ID is valid
    try:
        validation_usecase.isInternalCommunicationChannelVerified(
            secret=payload.secret
        )
        try:
            return isUserValid(session=session, id=payload.id)
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@private_router.delete("/logout")
def logout(
    token: str = Depends(validation_usecase.TokenValidation.is_token_invalid),
):
    return logout_usecase.logout(token=token)


@public_router.post("/get-user-by-id")
def get_private_user_by_id(
    session: Session = Depends(get_db), payload: InternalUserSchema = Body()
):
    try:
        validation_usecase.isInternalCommunicationChannelVerified(
            secret=payload.secret
        )
        # try:
        return profile_usecase.get_private_user_from_id(
            session=session, id=payload.id
        )

    except CommunicationChannelNotVerifiedException as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@public_router.get("/health-check")
def health_check():
    return {"status": "OK"}
