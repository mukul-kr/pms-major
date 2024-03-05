from settings import INTERNAL_COMMUNICATION_SECRET
from exception.validation import CommunicationChannelNotVerifiedException


def isInternalCommunicationChannelVerified(secret: str) -> bool:
    if INTERNAL_COMMUNICATION_SECRET == secret:
        return True
    else:
        raise CommunicationChannelNotVerifiedException("Invalid secret")
