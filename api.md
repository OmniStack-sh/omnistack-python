# Connect

Types:

```python
from omnistack.types import (
    ModelProviderDetails,
    ConnectListResponse,
    ConnectDeleteResponse,
    ConnectDeployResponse,
    ConnectFetchExternalProviderResponse,
)
```

Methods:

- <code title="get /{workspace_id}/connect/">client.connect.<a href="./src/omnistack/resources/connect.py">list</a>(workspace_id, \*\*<a href="src/omnistack/types/connect_list_params.py">params</a>) -> <a href="./src/omnistack/types/connect_list_response.py">ConnectListResponse</a></code>
- <code title="delete /{workspace_id}/connect/{omni_model_id}">client.connect.<a href="./src/omnistack/resources/connect.py">delete</a>(omni_model_id, \*, workspace_id) -> <a href="./src/omnistack/types/connect_delete_response.py">ConnectDeleteResponse</a></code>
- <code title="post /{workspace_id}/connect/deploy">client.connect.<a href="./src/omnistack/resources/connect.py">deploy</a>(workspace_id, \*\*<a href="src/omnistack/types/connect_deploy_params.py">params</a>) -> <a href="./src/omnistack/types/connect_deploy_response.py">ConnectDeployResponse</a></code>
- <code title="post /{workspace_id}/connect/fetch_external_provider">client.connect.<a href="./src/omnistack/resources/connect.py">fetch_external_provider</a>(workspace_id, \*\*<a href="src/omnistack/types/connect_fetch_external_provider_params.py">params</a>) -> <a href="./src/omnistack/types/connect_fetch_external_provider_response.py">ConnectFetchExternalProviderResponse</a></code>

# CustomModels

Types:

```python
from omnistack.types import (
    CustomModelRetrieveResponse,
    CustomModelListResponse,
    CustomModelDeleteResponse,
    CustomModelDeployResponse,
    CustomModelFetchCustomModelResponse,
)
```

Methods:

- <code title="get /{workspace_id}/custom_model/{omni_model_id}">client.custom_models.<a href="./src/omnistack/resources/custom_models.py">retrieve</a>(omni_model_id, \*, workspace_id) -> <a href="./src/omnistack/types/custom_model_retrieve_response.py">CustomModelRetrieveResponse</a></code>
- <code title="get /{workspace_id}/custom_model/">client.custom_models.<a href="./src/omnistack/resources/custom_models.py">list</a>(workspace_id) -> <a href="./src/omnistack/types/custom_model_list_response.py">CustomModelListResponse</a></code>
- <code title="delete /{workspace_id}/custom_model/{omni_model_id}">client.custom_models.<a href="./src/omnistack/resources/custom_models.py">delete</a>(omni_model_id, \*, workspace_id) -> <a href="./src/omnistack/types/custom_model_delete_response.py">CustomModelDeleteResponse</a></code>
- <code title="post /{workspace_id}/custom_model/deploy">client.custom_models.<a href="./src/omnistack/resources/custom_models.py">deploy</a>(workspace_id, \*\*<a href="src/omnistack/types/custom_model_deploy_params.py">params</a>) -> <a href="./src/omnistack/types/custom_model_deploy_response.py">CustomModelDeployResponse</a></code>
- <code title="post /{workspace_id}/custom_model/fetch_custom_model">client.custom_models.<a href="./src/omnistack/resources/custom_models.py">fetch_custom_model</a>(workspace_id, \*\*<a href="src/omnistack/types/custom_model_fetch_custom_model_params.py">params</a>) -> <a href="./src/omnistack/types/custom_model_fetch_custom_model_response.py">CustomModelFetchCustomModelResponse</a></code>

# Proxies

Types:

```python
from omnistack.types import Proxy
```

Methods:

- <code title="get /{workspace_id}/proxy/">client.proxies.<a href="./src/omnistack/resources/proxies.py">list</a>(workspace_id, \*\*<a href="src/omnistack/types/proxy_list_params.py">params</a>) -> <a href="./src/omnistack/types/proxy.py">Proxy</a></code>

# OmniProxies

Types:

```python
from omnistack.types import OmniProxyCreateResponse, OmniProxyDeleteResponse
```

Methods:

- <code title="post /{workspace_id}/proxy/">client.omni_proxies.<a href="./src/omnistack/resources/omni_proxies.py">create</a>(workspace_id, \*\*<a href="src/omnistack/types/omni_proxy_create_params.py">params</a>) -> <a href="./src/omnistack/types/omni_proxy_create_response.py">OmniProxyCreateResponse</a></code>
- <code title="delete /{workspace_id}/proxy/{omni_model_id}">client.omni_proxies.<a href="./src/omnistack/resources/omni_proxies.py">delete</a>(omni_model_id, \*, workspace_id) -> <a href="./src/omnistack/types/omni_proxy_delete_response.py">OmniProxyDeleteResponse</a></code>

# OpenAI

## Chat

Types:

```python
from omnistack.types.openai import ChatCompletionsResponse
```

Methods:

- <code title="post /openai/v1/chat/completions">client.openai.chat.<a href="./src/omnistack/resources/openai/chat.py">completions</a>(\*\*<a href="src/omnistack/types/openai/chat_completions_params.py">params</a>) -> <a href="./src/omnistack/types/openai/chat_completions_response.py">object</a></code>

## Completions

Types:

```python
from omnistack.types.openai import CompletionCreateResponse
```

Methods:

- <code title="post /openai/v1/completions">client.openai.completions.<a href="./src/omnistack/resources/openai/completions.py">create</a>(\*\*<a href="src/omnistack/types/openai/completion_create_params.py">params</a>) -> <a href="./src/omnistack/types/openai/completion_create_response.py">object</a></code>

# Users

Types:

```python
from omnistack.types import UserRetrieveResponse, UserLoginResponse
```

Methods:

- <code title="get /account/user/">client.users.<a href="./src/omnistack/resources/users.py">retrieve</a>() -> <a href="./src/omnistack/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="post /account/user/login">client.users.<a href="./src/omnistack/resources/users.py">login</a>(\*\*<a href="src/omnistack/types/user_login_params.py">params</a>) -> <a href="./src/omnistack/types/user_login_response.py">UserLoginResponse</a></code>

# Workspaces

## APIKeys

### Simple

Types:

```python
from omnistack.types.workspaces.api_keys import (
    SimpleCreateResponse,
    SimpleListResponse,
    SimpleDeleteResponse,
)
```

Methods:

- <code title="post /{workspace_id}/apikey/simple/create">client.workspaces.api_keys.simple.<a href="./src/omnistack/resources/workspaces/api_keys/simple.py">create</a>(workspace_id, \*\*<a href="src/omnistack/types/workspaces/api_keys/simple_create_params.py">params</a>) -> <a href="./src/omnistack/types/workspaces/api_keys/simple_create_response.py">SimpleCreateResponse</a></code>
- <code title="get /{workspace_id}/apikey/simple/">client.workspaces.api_keys.simple.<a href="./src/omnistack/resources/workspaces/api_keys/simple.py">list</a>(workspace_id) -> <a href="./src/omnistack/types/workspaces/api_keys/simple_list_response.py">SimpleListResponse</a></code>
- <code title="delete /{workspace_id}/apikey/simple/{api_key_id}">client.workspaces.api_keys.simple.<a href="./src/omnistack/resources/workspaces/api_keys/simple.py">delete</a>(api_key_id, \*, workspace_id) -> <a href="./src/omnistack/types/workspaces/api_keys/simple_delete_response.py">SimpleDeleteResponse</a></code>

## Evals

### External

Types:

```python
from omnistack.types.workspaces.evals import ExternalCreateResponse
```

Methods:

- <code title="post /{workspace_id}/eval/external/">client.workspaces.evals.external.<a href="./src/omnistack/resources/workspaces/evals/external.py">create</a>(workspace_id, \*\*<a href="src/omnistack/types/workspaces/evals/external_create_params.py">params</a>) -> <a href="./src/omnistack/types/workspaces/evals/external_create_response.py">object</a></code>

# ModelsDashboardOverview

Types:

```python
from omnistack.types import (
    BasicStats,
    CostPerRequest,
    LatencyPerRequest,
    RequestCountryDistribution,
    RequestData,
    TimeToFirstToken,
    TokensPerRequest,
    ModelsDashboardOverviewRetrieveResponse,
    ModelsDashboardOverviewCostPerRequestResponse,
    ModelsDashboardOverviewLatencyPerRequestResponse,
)
```

Methods:

- <code title="get /{workspace_id}/models/dashboard/{omni_model_id}/overview/">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">retrieve</a>(omni_model_id, \*, workspace_id) -> <a href="./src/omnistack/types/models_dashboard_overview_retrieve_response.py">ModelsDashboardOverviewRetrieveResponse</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/basic_stats">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">basic_stats</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_basic_stats_params.py">params</a>) -> <a href="./src/omnistack/types/basic_stats.py">BasicStats</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/cost_per_request">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">cost_per_request</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_cost_per_request_params.py">params</a>) -> <a href="./src/omnistack/types/models_dashboard_overview_cost_per_request_response.py">ModelsDashboardOverviewCostPerRequestResponse</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/latency_per_request">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">latency_per_request</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_latency_per_request_params.py">params</a>) -> <a href="./src/omnistack/types/models_dashboard_overview_latency_per_request_response.py">ModelsDashboardOverviewLatencyPerRequestResponse</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/request">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">request</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_request_params.py">params</a>) -> <a href="./src/omnistack/types/request_data.py">RequestData</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/request_country_distribution">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">request_country_distribution</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_request_country_distribution_params.py">params</a>) -> <a href="./src/omnistack/types/request_country_distribution.py">RequestCountryDistribution</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/time_to_first_token">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">time_to_first_token</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_time_to_first_token_params.py">params</a>) -> <a href="./src/omnistack/types/time_to_first_token.py">TimeToFirstToken</a></code>
- <code title="post /{workspace_id}/models/dashboard/{omni_model_id}/overview/tokens_per_request">client.models_dashboard_overview.<a href="./src/omnistack/resources/models_dashboard_overview.py">tokens_per_request</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/models_dashboard_overview_tokens_per_request_params.py">params</a>) -> <a href="./src/omnistack/types/tokens_per_request.py">TokensPerRequest</a></code>

# Observability

Types:

```python
from omnistack.types import ObservabilityInferenceResponse
```

Methods:

- <code title="get /{workspace_id}/observability/{omni_model_id}/inference">client.observability.<a href="./src/omnistack/resources/observability.py">inference</a>(omni_model_id, \*, workspace_id, \*\*<a href="src/omnistack/types/observability_inference_params.py">params</a>) -> <a href="./src/omnistack/types/observability_inference_response.py">object</a></code>

# Models

Types:

```python
from omnistack.types import ModelListResponse
```

Methods:

- <code title="get /{workspace_id}/models/">client.models.<a href="./src/omnistack/resources/models.py">list</a>(workspace_id) -> <a href="./src/omnistack/types/model_list_response.py">ModelListResponse</a></code>

# Explore

Types:

```python
from omnistack.types import ExploreModelResponse
```

Methods:

- <code title="get /{workspace_id}/models/explore/">client.explore.<a href="./src/omnistack/resources/explore.py">list</a>(workspace_id) -> <a href="./src/omnistack/types/explore_model_response.py">ExploreModelResponse</a></code>

# Projects

Types:

```python
from omnistack.types import GetProjectsResponse, ProjectCreateResponse, ProjectListResponse
```

Methods:

- <code title="post /{workspace_id}/projects/">client.projects.<a href="./src/omnistack/resources/projects/projects.py">create</a>(workspace_id, \*\*<a href="src/omnistack/types/project_create_params.py">params</a>) -> <a href="./src/omnistack/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="get /{workspace_id}/projects/">client.projects.<a href="./src/omnistack/resources/projects/projects.py">list</a>(workspace_id) -> <a href="./src/omnistack/types/project_list_response.py">ProjectListResponse</a></code>

## Prompts

Types:

```python
from omnistack.types.projects import (
    CreatePromptResponse,
    GetPromptResponse,
    GetPromptsResponse,
    PromptUpdateResponse,
    PromptListResponse,
    PromptDeleteResponse,
    PromptSwitchVersionResponse,
)
```

Methods:

- <code title="post /{workspace_id}/projects/{project_id}/prompts/">client.projects.prompts.<a href="./src/omnistack/resources/projects/prompts.py">create</a>(project_id, \*, workspace_id, \*\*<a href="src/omnistack/types/projects/prompt_create_params.py">params</a>) -> <a href="./src/omnistack/types/projects/create_prompt_response.py">CreatePromptResponse</a></code>
- <code title="get /{workspace_id}/projects/{project_id}/prompts/{prompt_id}/">client.projects.prompts.<a href="./src/omnistack/resources/projects/prompts.py">retrieve</a>(prompt_id, \*, workspace_id, project_id, \*\*<a href="src/omnistack/types/projects/prompt_retrieve_params.py">params</a>) -> <a href="./src/omnistack/types/projects/get_prompt_response.py">GetPromptResponse</a></code>
- <code title="post /{workspace_id}/projects/{project_id}/prompts/{prompt_id}/">client.projects.prompts.<a href="./src/omnistack/resources/projects/prompts.py">update</a>(prompt_id, \*, workspace_id, project_id, \*\*<a href="src/omnistack/types/projects/prompt_update_params.py">params</a>) -> <a href="./src/omnistack/types/projects/prompt_update_response.py">PromptUpdateResponse</a></code>
- <code title="get /{workspace_id}/projects/{project_id}/prompts/">client.projects.prompts.<a href="./src/omnistack/resources/projects/prompts.py">list</a>(project_id, \*, workspace_id) -> <a href="./src/omnistack/types/projects/prompt_list_response.py">PromptListResponse</a></code>
- <code title="delete /{workspace_id}/projects/{project_id}/prompts/{prompt_id}/">client.projects.prompts.<a href="./src/omnistack/resources/projects/prompts.py">delete</a>(prompt_id, \*, workspace_id, project_id) -> <a href="./src/omnistack/types/projects/prompt_delete_response.py">PromptDeleteResponse</a></code>
- <code title="post /{workspace_id}/projects/{project_id}/prompts/{prompt_id}/switch_version">client.projects.prompts.<a href="./src/omnistack/resources/projects/prompts.py">switch_version</a>(prompt_id, \*, workspace_id, project_id, \*\*<a href="src/omnistack/types/projects/prompt_switch_version_params.py">params</a>) -> <a href="./src/omnistack/types/projects/prompt_switch_version_response.py">PromptSwitchVersionResponse</a></code>

## Playground

Types:

```python
from omnistack.types.projects import PlaygroundRetrieveResponse
```

Methods:

- <code title="get /{workspace_id}/projects/{project_id}/playground/">client.projects.playground.<a href="./src/omnistack/resources/projects/playground.py">retrieve</a>(project_id, \*, workspace_id) -> <a href="./src/omnistack/types/projects/playground_retrieve_response.py">object</a></code>

# Home

Types:

```python
from omnistack.types import HomeRetrieveResponse
```

Methods:

- <code title="get /">client.home.<a href="./src/omnistack/resources/home.py">retrieve</a>() -> <a href="./src/omnistack/types/home_retrieve_response.py">object</a></code>
