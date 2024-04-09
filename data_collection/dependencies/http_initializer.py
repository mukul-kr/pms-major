import requests
from settings import INTERNAL_COMMUNICATION_URL


class HTTPClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request error: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    def get(self, endpoint):
        return self._make_request("GET", endpoint)

    def post(self, endpoint, data=None):
        return self._make_request("POST", endpoint, data)

    def put(self, endpoint, data=None):
        return self._make_request("PUT", endpoint, data)

    def delete(self, endpoint):
        return self._make_request("DELETE", endpoint)


class AuthClient(HTTPClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def post_validate_user(self, payload):
        return self.post("auth/validate-user", payload)

    def post_get_user_by_id(self, payload):
        return self.post("auth/get-user-by-id", payload)

    def get_health_check(self):
        return self.get("health-check")


class NotificationClient(HTTPClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def post_device_off_notification(self, payload):
        return self.post("notification/notify", payload)

    def get_health_check(self):
        return self.get("health-check")


class DataClient(HTTPClient):
    def __init__(self, base_url):
        super().__init__(base_url)

    def post_execute_device_off_check(self, payload):
        return self.post("api/notify-dead-device", payload)

    def get_health_check(self):
        return self.get("health-check")


authClient = AuthClient(INTERNAL_COMMUNICATION_URL)
notificationClient = NotificationClient(INTERNAL_COMMUNICATION_URL)
dataClient = DataClient(INTERNAL_COMMUNICATION_URL)
