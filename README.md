# agent-identity-sdk
Build seamless identity-aware integrations for LLM agents

## Usage

### Initialization

```py
from agent_identity_sdk import AgentIdentity
from dotenv import load_dotenv
import os

config = {
   "agent_id": os.getenv("AGENT_ID"),
   "agent_secret": os.getenv("AGENT_SECRET")
}

agent = AgentIdentity(config)
```

Once the agent is created, its instance methods can be used to invoke authentication.

### Get access token

```py
token = agent.getAccessToken(authz_code)
```

### Refresh access token

```py
code_verifier = "<code_verifier>" # code verifier to pass when PKCE is enabled
authz_code = "<authorization_code>" # authorization code received at the callback URL 
refresh_token = "<refresh_token>" # refresh token to be used to refresh access token

token = agent.getAccessToken(authz_code, code_verifier, refresh_token)
```

### Initiate on-behalf-of authentication

```py
connection = "gmail";
scopes = (
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.labels",
)

agent.initOnBehalfOfAuth(connection,scopes)
```

## Initiate async authentication

```bash
username = "johndoe@example.com" # The user for which the async authentication flow should be initiated

agent.initAsyncAuth(username)
```