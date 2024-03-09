from . import get_public_router

import logging

# Create a custom logger
logger = logging.getLogger(__name__)
from fastapi import HTTPException, Body


from dependencies.email_intializer import CreateUserEmail, EventNotTriggered, DataWarning

from domain.usecase import sendemail, validation_usecase

from schemas.email import EmailResponseSchema, EmailSchema

public_router = get_public_router()


@public_router.post("/notify", response_model=EmailResponseSchema)
def validate_user(
    payload: EmailSchema = Body(),
):
    # Implement logic to check if the user ID is valid
    try:
        validation_usecase.isInternalCommunicationChannelVerified(
            secret=payload.secret
        )
        try:
            if payload.event == CreateUserEmail["Event-Name"]:
                sendemail.sendMail(
                    To=payload.email,
                    Subject=CreateUserEmail["Subject"],
                    Content=CreateUserEmail["Content"],
                    name=payload.name,
                    additionalProp1=payload.additionalProp1,  # type: ignore
                )
                return EmailResponseSchema(status="success")
            elif payload.event == EventNotTriggered["Event-Name"]:
                sendemail.sendMail(
                    To=payload.email,
                    Subject=EventNotTriggered["Subject"],
                    Content=EventNotTriggered["Content"],
                    name=payload.name,
                    additionalProp1=payload.additionalProp1,  # type: ignore
                )
                return EmailResponseSchema(status="success")
            elif payload.event == DataWarning["Event-Name"]:
                sendemail.sendMail(
                    To=payload.email,
                    Subject=DataWarning["Subject"],
                    Content=DataWarning["Content"],
                    name=payload.name,
                    additionalProp1=payload.additionalProp1,  # type: ignore
                )
                return EmailResponseSchema(status="success")
        except Exception as e:
            logger.error(f"error sending mails. Error : {e}")
            return EmailResponseSchema(status="failure")

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@public_router.get("/health-check")
def health_check():
    return {"status": "OK"}
