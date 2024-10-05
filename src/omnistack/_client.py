# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OmnistackError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Omnistack",
    "AsyncOmnistack",
    "Client",
    "AsyncClient",
]


class Omnistack(SyncAPIClient):
    connect: resources.ConnectResource
    custom_models: resources.CustomModelsResource
    proxies: resources.ProxiesResource
    omni_proxies: resources.OmniProxiesResource
    openai: resources.OpenAIResource
    users: resources.UsersResource
    workspaces: resources.WorkspacesResource
    models_dashboard_overview: resources.ModelsDashboardOverviewResource
    observability: resources.ObservabilityResource
    models: resources.ModelsResource
    explore: resources.ExploreResource
    projects: resources.ProjectsResource
    home: resources.HomeResource
    with_raw_response: OmnistackWithRawResponse
    with_streaming_response: OmnistackWithStreamedResponse

    # client options
    jwt_bearer_token: str

    def __init__(
        self,
        *,
        jwt_bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous omnistack client instance.

        This automatically infers the `jwt_bearer_token` argument from the `JWT_BEARER_TOKEN` environment variable if it is not provided.
        """
        if jwt_bearer_token is None:
            jwt_bearer_token = os.environ.get("JWT_BEARER_TOKEN")
        if jwt_bearer_token is None:
            raise OmnistackError(
                "The jwt_bearer_token client option must be set either by passing jwt_bearer_token to the client or by setting the JWT_BEARER_TOKEN environment variable"
            )
        self.jwt_bearer_token = jwt_bearer_token

        if base_url is None:
            base_url = os.environ.get("OMNISTACK_BASE_URL")
        if base_url is None:
            base_url = f"https://localhost:8080/test-api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.connect = resources.ConnectResource(self)
        self.custom_models = resources.CustomModelsResource(self)
        self.proxies = resources.ProxiesResource(self)
        self.omni_proxies = resources.OmniProxiesResource(self)
        self.openai = resources.OpenAIResource(self)
        self.users = resources.UsersResource(self)
        self.workspaces = resources.WorkspacesResource(self)
        self.models_dashboard_overview = resources.ModelsDashboardOverviewResource(self)
        self.observability = resources.ObservabilityResource(self)
        self.models = resources.ModelsResource(self)
        self.explore = resources.ExploreResource(self)
        self.projects = resources.ProjectsResource(self)
        self.home = resources.HomeResource(self)
        self.with_raw_response = OmnistackWithRawResponse(self)
        self.with_streaming_response = OmnistackWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        jwt_bearer_token = self.jwt_bearer_token
        return {"Authorization": f"Bearer {jwt_bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        jwt_bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            jwt_bearer_token=jwt_bearer_token or self.jwt_bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOmnistack(AsyncAPIClient):
    connect: resources.AsyncConnectResource
    custom_models: resources.AsyncCustomModelsResource
    proxies: resources.AsyncProxiesResource
    omni_proxies: resources.AsyncOmniProxiesResource
    openai: resources.AsyncOpenAIResource
    users: resources.AsyncUsersResource
    workspaces: resources.AsyncWorkspacesResource
    models_dashboard_overview: resources.AsyncModelsDashboardOverviewResource
    observability: resources.AsyncObservabilityResource
    models: resources.AsyncModelsResource
    explore: resources.AsyncExploreResource
    projects: resources.AsyncProjectsResource
    home: resources.AsyncHomeResource
    with_raw_response: AsyncOmnistackWithRawResponse
    with_streaming_response: AsyncOmnistackWithStreamedResponse

    # client options
    jwt_bearer_token: str

    def __init__(
        self,
        *,
        jwt_bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async omnistack client instance.

        This automatically infers the `jwt_bearer_token` argument from the `JWT_BEARER_TOKEN` environment variable if it is not provided.
        """
        if jwt_bearer_token is None:
            jwt_bearer_token = os.environ.get("JWT_BEARER_TOKEN")
        if jwt_bearer_token is None:
            raise OmnistackError(
                "The jwt_bearer_token client option must be set either by passing jwt_bearer_token to the client or by setting the JWT_BEARER_TOKEN environment variable"
            )
        self.jwt_bearer_token = jwt_bearer_token

        if base_url is None:
            base_url = os.environ.get("OMNISTACK_BASE_URL")
        if base_url is None:
            base_url = f"https://localhost:8080/test-api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.connect = resources.AsyncConnectResource(self)
        self.custom_models = resources.AsyncCustomModelsResource(self)
        self.proxies = resources.AsyncProxiesResource(self)
        self.omni_proxies = resources.AsyncOmniProxiesResource(self)
        self.openai = resources.AsyncOpenAIResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.workspaces = resources.AsyncWorkspacesResource(self)
        self.models_dashboard_overview = resources.AsyncModelsDashboardOverviewResource(self)
        self.observability = resources.AsyncObservabilityResource(self)
        self.models = resources.AsyncModelsResource(self)
        self.explore = resources.AsyncExploreResource(self)
        self.projects = resources.AsyncProjectsResource(self)
        self.home = resources.AsyncHomeResource(self)
        self.with_raw_response = AsyncOmnistackWithRawResponse(self)
        self.with_streaming_response = AsyncOmnistackWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        jwt_bearer_token = self.jwt_bearer_token
        return {"Authorization": f"Bearer {jwt_bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        jwt_bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            jwt_bearer_token=jwt_bearer_token or self.jwt_bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OmnistackWithRawResponse:
    def __init__(self, client: Omnistack) -> None:
        self.connect = resources.ConnectResourceWithRawResponse(client.connect)
        self.custom_models = resources.CustomModelsResourceWithRawResponse(client.custom_models)
        self.proxies = resources.ProxiesResourceWithRawResponse(client.proxies)
        self.omni_proxies = resources.OmniProxiesResourceWithRawResponse(client.omni_proxies)
        self.openai = resources.OpenAIResourceWithRawResponse(client.openai)
        self.users = resources.UsersResourceWithRawResponse(client.users)
        self.workspaces = resources.WorkspacesResourceWithRawResponse(client.workspaces)
        self.models_dashboard_overview = resources.ModelsDashboardOverviewResourceWithRawResponse(
            client.models_dashboard_overview
        )
        self.observability = resources.ObservabilityResourceWithRawResponse(client.observability)
        self.models = resources.ModelsResourceWithRawResponse(client.models)
        self.explore = resources.ExploreResourceWithRawResponse(client.explore)
        self.projects = resources.ProjectsResourceWithRawResponse(client.projects)
        self.home = resources.HomeResourceWithRawResponse(client.home)


class AsyncOmnistackWithRawResponse:
    def __init__(self, client: AsyncOmnistack) -> None:
        self.connect = resources.AsyncConnectResourceWithRawResponse(client.connect)
        self.custom_models = resources.AsyncCustomModelsResourceWithRawResponse(client.custom_models)
        self.proxies = resources.AsyncProxiesResourceWithRawResponse(client.proxies)
        self.omni_proxies = resources.AsyncOmniProxiesResourceWithRawResponse(client.omni_proxies)
        self.openai = resources.AsyncOpenAIResourceWithRawResponse(client.openai)
        self.users = resources.AsyncUsersResourceWithRawResponse(client.users)
        self.workspaces = resources.AsyncWorkspacesResourceWithRawResponse(client.workspaces)
        self.models_dashboard_overview = resources.AsyncModelsDashboardOverviewResourceWithRawResponse(
            client.models_dashboard_overview
        )
        self.observability = resources.AsyncObservabilityResourceWithRawResponse(client.observability)
        self.models = resources.AsyncModelsResourceWithRawResponse(client.models)
        self.explore = resources.AsyncExploreResourceWithRawResponse(client.explore)
        self.projects = resources.AsyncProjectsResourceWithRawResponse(client.projects)
        self.home = resources.AsyncHomeResourceWithRawResponse(client.home)


class OmnistackWithStreamedResponse:
    def __init__(self, client: Omnistack) -> None:
        self.connect = resources.ConnectResourceWithStreamingResponse(client.connect)
        self.custom_models = resources.CustomModelsResourceWithStreamingResponse(client.custom_models)
        self.proxies = resources.ProxiesResourceWithStreamingResponse(client.proxies)
        self.omni_proxies = resources.OmniProxiesResourceWithStreamingResponse(client.omni_proxies)
        self.openai = resources.OpenAIResourceWithStreamingResponse(client.openai)
        self.users = resources.UsersResourceWithStreamingResponse(client.users)
        self.workspaces = resources.WorkspacesResourceWithStreamingResponse(client.workspaces)
        self.models_dashboard_overview = resources.ModelsDashboardOverviewResourceWithStreamingResponse(
            client.models_dashboard_overview
        )
        self.observability = resources.ObservabilityResourceWithStreamingResponse(client.observability)
        self.models = resources.ModelsResourceWithStreamingResponse(client.models)
        self.explore = resources.ExploreResourceWithStreamingResponse(client.explore)
        self.projects = resources.ProjectsResourceWithStreamingResponse(client.projects)
        self.home = resources.HomeResourceWithStreamingResponse(client.home)


class AsyncOmnistackWithStreamedResponse:
    def __init__(self, client: AsyncOmnistack) -> None:
        self.connect = resources.AsyncConnectResourceWithStreamingResponse(client.connect)
        self.custom_models = resources.AsyncCustomModelsResourceWithStreamingResponse(client.custom_models)
        self.proxies = resources.AsyncProxiesResourceWithStreamingResponse(client.proxies)
        self.omni_proxies = resources.AsyncOmniProxiesResourceWithStreamingResponse(client.omni_proxies)
        self.openai = resources.AsyncOpenAIResourceWithStreamingResponse(client.openai)
        self.users = resources.AsyncUsersResourceWithStreamingResponse(client.users)
        self.workspaces = resources.AsyncWorkspacesResourceWithStreamingResponse(client.workspaces)
        self.models_dashboard_overview = resources.AsyncModelsDashboardOverviewResourceWithStreamingResponse(
            client.models_dashboard_overview
        )
        self.observability = resources.AsyncObservabilityResourceWithStreamingResponse(client.observability)
        self.models = resources.AsyncModelsResourceWithStreamingResponse(client.models)
        self.explore = resources.AsyncExploreResourceWithStreamingResponse(client.explore)
        self.projects = resources.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.home = resources.AsyncHomeResourceWithStreamingResponse(client.home)


Client = Omnistack

AsyncClient = AsyncOmnistack
