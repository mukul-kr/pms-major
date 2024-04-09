from settings import INTERNAL_COMMUNICATION_SECRET
from dependencies.http_initializer import authClient
import logging

# Create a custom logger
logger = logging.getLogger(__name__)


def create_payload(user_id):
    return {"id": int(user_id), "secret": INTERNAL_COMMUNICATION_SECRET}


def validate_user(user_id: int) -> bool:
    try:
        response = authClient.post_validate_user(
            payload=create_payload(user_id)
        )
        if response.status_code == 200:
            result = response.json()
            if result["valid"]:
                return True
            else:
                return False
        else:
            logger.error(
                f"Request failed with status code: {response.status_code}"
            )
            return False

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return False
