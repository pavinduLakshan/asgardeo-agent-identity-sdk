# asgardeo-agent-identity-sdk
Secure LLM agents with Asgardeo

## Usage

### Initialize SDK

```py
from agent_identity_sdk import sdk

sdkConfig = {
    "org_name": "<your_asgardeo_org_name>",
    "base_url": "https://api.asgardeo.io/t/<your_asgardeo_org_name>" # optional
}

sdk.init(sdkConfig)
```

### Initialize an agent

#### Using agent ID and secret

```py
from agent_identity_sdk import AgentIdentity
from dotenv import load_dotenv
import os

# Using agent ID and agent secret
config = {
   "credential": {
    "agent_id": os.getenv("AGENT_ID"),
    "agent_secret": os.getenv("AGENT_SECRET")
   }
}
```

#### Using mTLS

```py
from agent_identity_sdk import AgentIdentity
from dotenv import load_dotenv
import os

config = {
   "credential": {
    "client_cert_path": os.getenv("AGENT_CERTIFICATE_PATH"),
    "client_key_path": os.getenv("AGENT_CERTIFICATE_KEY_PATH"),
    "ca_cert_path": os.getenv("AGENT_CA_CERTIFICATE_PATH")
   }
}

agent = AgentIdentity(config)
```

Once the agent is initialized, its instance methods can be used to invoke authentication.

### Get access token

```py
# Get an access token using agent's identity.
token = agent.getAccessToken()
```

```py
# Get an access token using authorization code grant.
options = {
  "authorization_code": "",
  "code_verifier": "" # optional, required when PKCE is enabled
}

token = agent.getAccessToken(options)
```

### Refresh access token

```py
# Get an access token via refresh token grant.
token = agent.refreshAccessToken(refresh_token)
```

### Initiate on-behalf-of authentication

1. For first party API

```py
on_behalf_of_auth_request = {
    "scopes": (
        "read_bookings",
        "create_bookings"
    )
}

agent.initOnBehalfOfAuth(on_behalf_of_auth_request)
```

2. For third party API

```py
on_behalf_of_auth_request = {
    connection = "gmail";
    scopes = (
        "https://www.googleapis.com/auth/gmail.readonly",
        "https://www.googleapis.com/auth/gmail.labels",
    )
}
agent.initOnBehalfOfAuth(on_behalf_of_auth_request)
```

### Async authentication

```bash
username = "johndoe@example.com" # The user for which the async authentication flow should be initiated

agent.initAsyncAuth(username)
```