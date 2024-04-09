class DeviceNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class DeviceAlreadyExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)


class DeviceNotCreatedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class DeviceCredentialNotMatchedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidUserIdException(Exception):
    def __init__(self, message):
        super().__init__(message)
