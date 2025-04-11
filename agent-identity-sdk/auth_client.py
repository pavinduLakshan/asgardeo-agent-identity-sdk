import requests

class AuthClient:
    """
    Authentication client for handling authentication flows in LLM agents.
    """

    def __init__(self, base_url: str, client_id: str, client_secret: str):
        self.base_url = base_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def authenticate(self) -> str:
        pass

    def get_headers(self) -> dict:
        """
        Return the auth headers to use in authenticated requests.
        """
        if not self.token:
