# agent-identity-sdk
Build seamless identity-aware integrations for LLM agents

## Usage

### Get access token

```bash
from agent_identity_sdk import AuthClient

token = AuthClient.getAccessToken(authz_code)
```

### Refresh access token

```bash
from agent_identity_sdk import AuthClient

code_verifier = "<code_verifier_when_PKCE_is_enabled"
authz_code = "<authorization_code_received_by_the_callback_url>" 
refresh_token = "<refresh_token_to_be_used_to_refresh_access_token>"

token = AuthClient.getAccessToken(authz_code, code_verifier, refresh_token)
```

### Initiate on-behalf-of authentication

```bash
from agent_identity_sdk import AuthClient

connection = "gmail";
scopes = (
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.labels",
)

AuthClient.initOnBehalfOfAuth(connection,scopes)
```

## Initiate async authentication

```bash
from agent_identity_sdk import AuthClient

username = "johndoe@example.com" # The user for which the async authentication flow should be initiated

AuthClient.initAsyncAuth(username)
```