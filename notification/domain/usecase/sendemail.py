import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
from fastapi import HTTPException
from jinja2 import Environment, select_autoescape

import logging
from settings import MAIL_PORT, MAIL_SMTP_SERVER, EMAIL, EMAIL_APP_PASSWORD

env = Environment(autoescape=select_autoescape())
logger = logging.getLogger(__name__)

context = ssl.create_default_context()


def createMessage(
    To: str,
    Subject: str,
    html: str,
    name: str = "",
    additionalProps: dict = {},
) -> MIMEMultipart:
    message = MIMEMultipart("alternative")
    try:
        template = env.from_string(html)
        additionalProps["name"] = name
        rendered_html_string = template.render(additionalProps)
        subject = env.from_string(Subject)
        Subject = subject.render(additionalProps)
        message["Subject"] = Subject
        message["From"] = EMAIL
        message["To"] = To
        html_content = MIMEText(rendered_html_string, "html")
        message.attach(html_content)
        return message
    except Exception as e:
        logger.error(f"error creating email message. Error : {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error creating email message. Error : {e}",
        )


def sendMail(
    To: str,
    Subject: str,
    Content: str,
    name: str = "",
    additionalProp1: dict = {},
) -> None:
    message = createMessage(To, Subject, Content, name, additionalProp1)
    with smtplib.SMTP_SSL(
        MAIL_SMTP_SERVER, int(MAIL_PORT), context=context
    ) as server:
        server.login(EMAIL, EMAIL_APP_PASSWORD)
        server.sendmail(EMAIL, To, message.as_string())
