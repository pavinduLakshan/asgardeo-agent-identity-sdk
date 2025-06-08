import os
import requests
from typing import Optional, Dict, Any

class SDK:
    _config = {}

    @classmethod
    def init(cls, config: Dict[str, str]):
        cls._config = config

class AgentIdentity:
    def __init__(self, config: Dict[str, Any]):
        self.credential = config.get("credential", {})
        self.token_endpoint = SDK._config.get("base_url", f"https://api.asgardeo.io/t/{SDK._config['org_name']}") + "/oauth2/token"

    def getAccessToken(self, options: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if options is None:
            # Client credentials grant
            data = {
                "grant_type": "client_credentials",
                "client_id": self.credential.get("agent_id"),
                "client_secret": self.credential.get("agent_secret")
            }
        else:
            # Authorization code grant
            data = {
                "grant_type": "authorization_code",
                "code": options.get("authorization_code"),
                "client_id": self.credential.get("agent_id"),
                "client_secret": self.credential.get("agent_secret"),
                "scope": " ".join(options.get("scopes", []))
            }
            if options.get("code_verifier"):
                data["code_verifier"] = options.get("code_verifier")

        response = requests.post(self.token_endpoint, data=data)
        return response.json()

    def refreshAccessToken(self, refresh_token: str) -> Dict[str, Any]:
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.credential.get("agent_id"),
            "client_secret": self.credential.get("agent_secret")
        }
        response = requests.post(self.token_endpoint, data=data)
        return response.json()

    def initOnBehalfOfAuth(self, request: Dict[str, Any], options: Optional[Dict[str, Any]] = None):
        async_mode = options.get("async") if options else False

        print("Initiating On-Behalf-Of Authentication")
        print("Scopes:", request.get("scopes"))

        if request.get("connection"):
            print("Connection:", request.get("connection"))

        if async_mode:
            print("Async mode enabled")
            print("Username:", request.get("username"))
