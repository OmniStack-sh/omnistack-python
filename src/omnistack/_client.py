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
    chats: resources.ChatsResource
    completions: resources.CompletionsResource
    images: resources.ImagesResource
    embeddings: resources.EmbeddingsResource
    audio: resources.AudioResource
    files: resources.FilesResource
    uploads: resources.UploadsResource
    fine_tuning: resources.FineTuningResource
    models: resources.ModelsResource
    moderations: resources.ModerationsResource
    assistants: resources.AssistantsResource
    threads: resources.ThreadsResource
    vector_stores: resources.VectorStoresResource
    batches: resources.BatchesResource
    organization: resources.OrganizationResource
    projects: resources.ProjectsResource
    with_raw_response: OmnistackWithRawResponse
    with_streaming_response: OmnistackWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
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

        This automatically infers the `bearer_token` argument from the `BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise OmnistackError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("OMNISTACK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openai.com/v1"

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

        self.chats = resources.ChatsResource(self)
        self.completions = resources.CompletionsResource(self)
        self.images = resources.ImagesResource(self)
        self.embeddings = resources.EmbeddingsResource(self)
        self.audio = resources.AudioResource(self)
        self.files = resources.FilesResource(self)
        self.uploads = resources.UploadsResource(self)
        self.fine_tuning = resources.FineTuningResource(self)
        self.models = resources.ModelsResource(self)
        self.moderations = resources.ModerationsResource(self)
        self.assistants = resources.AssistantsResource(self)
        self.threads = resources.ThreadsResource(self)
        self.vector_stores = resources.VectorStoresResource(self)
        self.batches = resources.BatchesResource(self)
        self.organization = resources.OrganizationResource(self)
        self.projects = resources.ProjectsResource(self)
        self.with_raw_response = OmnistackWithRawResponse(self)
        self.with_streaming_response = OmnistackWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

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
        bearer_token: str | None = None,
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
            bearer_token=bearer_token or self.bearer_token,
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
    chats: resources.AsyncChatsResource
    completions: resources.AsyncCompletionsResource
    images: resources.AsyncImagesResource
    embeddings: resources.AsyncEmbeddingsResource
    audio: resources.AsyncAudioResource
    files: resources.AsyncFilesResource
    uploads: resources.AsyncUploadsResource
    fine_tuning: resources.AsyncFineTuningResource
    models: resources.AsyncModelsResource
    moderations: resources.AsyncModerationsResource
    assistants: resources.AsyncAssistantsResource
    threads: resources.AsyncThreadsResource
    vector_stores: resources.AsyncVectorStoresResource
    batches: resources.AsyncBatchesResource
    organization: resources.AsyncOrganizationResource
    projects: resources.AsyncProjectsResource
    with_raw_response: AsyncOmnistackWithRawResponse
    with_streaming_response: AsyncOmnistackWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
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

        This automatically infers the `bearer_token` argument from the `BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("BEARER_TOKEN")
        if bearer_token is None:
            raise OmnistackError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("OMNISTACK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.openai.com/v1"

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

        self.chats = resources.AsyncChatsResource(self)
        self.completions = resources.AsyncCompletionsResource(self)
        self.images = resources.AsyncImagesResource(self)
        self.embeddings = resources.AsyncEmbeddingsResource(self)
        self.audio = resources.AsyncAudioResource(self)
        self.files = resources.AsyncFilesResource(self)
        self.uploads = resources.AsyncUploadsResource(self)
        self.fine_tuning = resources.AsyncFineTuningResource(self)
        self.models = resources.AsyncModelsResource(self)
        self.moderations = resources.AsyncModerationsResource(self)
        self.assistants = resources.AsyncAssistantsResource(self)
        self.threads = resources.AsyncThreadsResource(self)
        self.vector_stores = resources.AsyncVectorStoresResource(self)
        self.batches = resources.AsyncBatchesResource(self)
        self.organization = resources.AsyncOrganizationResource(self)
        self.projects = resources.AsyncProjectsResource(self)
        self.with_raw_response = AsyncOmnistackWithRawResponse(self)
        self.with_streaming_response = AsyncOmnistackWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

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
        bearer_token: str | None = None,
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
            bearer_token=bearer_token or self.bearer_token,
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
        self.chats = resources.ChatsResourceWithRawResponse(client.chats)
        self.completions = resources.CompletionsResourceWithRawResponse(client.completions)
        self.images = resources.ImagesResourceWithRawResponse(client.images)
        self.embeddings = resources.EmbeddingsResourceWithRawResponse(client.embeddings)
        self.audio = resources.AudioResourceWithRawResponse(client.audio)
        self.files = resources.FilesResourceWithRawResponse(client.files)
        self.uploads = resources.UploadsResourceWithRawResponse(client.uploads)
        self.fine_tuning = resources.FineTuningResourceWithRawResponse(client.fine_tuning)
        self.models = resources.ModelsResourceWithRawResponse(client.models)
        self.moderations = resources.ModerationsResourceWithRawResponse(client.moderations)
        self.assistants = resources.AssistantsResourceWithRawResponse(client.assistants)
        self.threads = resources.ThreadsResourceWithRawResponse(client.threads)
        self.vector_stores = resources.VectorStoresResourceWithRawResponse(client.vector_stores)
        self.batches = resources.BatchesResourceWithRawResponse(client.batches)
        self.organization = resources.OrganizationResourceWithRawResponse(client.organization)
        self.projects = resources.ProjectsResourceWithRawResponse(client.projects)


class AsyncOmnistackWithRawResponse:
    def __init__(self, client: AsyncOmnistack) -> None:
        self.chats = resources.AsyncChatsResourceWithRawResponse(client.chats)
        self.completions = resources.AsyncCompletionsResourceWithRawResponse(client.completions)
        self.images = resources.AsyncImagesResourceWithRawResponse(client.images)
        self.embeddings = resources.AsyncEmbeddingsResourceWithRawResponse(client.embeddings)
        self.audio = resources.AsyncAudioResourceWithRawResponse(client.audio)
        self.files = resources.AsyncFilesResourceWithRawResponse(client.files)
        self.uploads = resources.AsyncUploadsResourceWithRawResponse(client.uploads)
        self.fine_tuning = resources.AsyncFineTuningResourceWithRawResponse(client.fine_tuning)
        self.models = resources.AsyncModelsResourceWithRawResponse(client.models)
        self.moderations = resources.AsyncModerationsResourceWithRawResponse(client.moderations)
        self.assistants = resources.AsyncAssistantsResourceWithRawResponse(client.assistants)
        self.threads = resources.AsyncThreadsResourceWithRawResponse(client.threads)
        self.vector_stores = resources.AsyncVectorStoresResourceWithRawResponse(client.vector_stores)
        self.batches = resources.AsyncBatchesResourceWithRawResponse(client.batches)
        self.organization = resources.AsyncOrganizationResourceWithRawResponse(client.organization)
        self.projects = resources.AsyncProjectsResourceWithRawResponse(client.projects)


class OmnistackWithStreamedResponse:
    def __init__(self, client: Omnistack) -> None:
        self.chats = resources.ChatsResourceWithStreamingResponse(client.chats)
        self.completions = resources.CompletionsResourceWithStreamingResponse(client.completions)
        self.images = resources.ImagesResourceWithStreamingResponse(client.images)
        self.embeddings = resources.EmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.audio = resources.AudioResourceWithStreamingResponse(client.audio)
        self.files = resources.FilesResourceWithStreamingResponse(client.files)
        self.uploads = resources.UploadsResourceWithStreamingResponse(client.uploads)
        self.fine_tuning = resources.FineTuningResourceWithStreamingResponse(client.fine_tuning)
        self.models = resources.ModelsResourceWithStreamingResponse(client.models)
        self.moderations = resources.ModerationsResourceWithStreamingResponse(client.moderations)
        self.assistants = resources.AssistantsResourceWithStreamingResponse(client.assistants)
        self.threads = resources.ThreadsResourceWithStreamingResponse(client.threads)
        self.vector_stores = resources.VectorStoresResourceWithStreamingResponse(client.vector_stores)
        self.batches = resources.BatchesResourceWithStreamingResponse(client.batches)
        self.organization = resources.OrganizationResourceWithStreamingResponse(client.organization)
        self.projects = resources.ProjectsResourceWithStreamingResponse(client.projects)


class AsyncOmnistackWithStreamedResponse:
    def __init__(self, client: AsyncOmnistack) -> None:
        self.chats = resources.AsyncChatsResourceWithStreamingResponse(client.chats)
        self.completions = resources.AsyncCompletionsResourceWithStreamingResponse(client.completions)
        self.images = resources.AsyncImagesResourceWithStreamingResponse(client.images)
        self.embeddings = resources.AsyncEmbeddingsResourceWithStreamingResponse(client.embeddings)
        self.audio = resources.AsyncAudioResourceWithStreamingResponse(client.audio)
        self.files = resources.AsyncFilesResourceWithStreamingResponse(client.files)
        self.uploads = resources.AsyncUploadsResourceWithStreamingResponse(client.uploads)
        self.fine_tuning = resources.AsyncFineTuningResourceWithStreamingResponse(client.fine_tuning)
        self.models = resources.AsyncModelsResourceWithStreamingResponse(client.models)
        self.moderations = resources.AsyncModerationsResourceWithStreamingResponse(client.moderations)
        self.assistants = resources.AsyncAssistantsResourceWithStreamingResponse(client.assistants)
        self.threads = resources.AsyncThreadsResourceWithStreamingResponse(client.threads)
        self.vector_stores = resources.AsyncVectorStoresResourceWithStreamingResponse(client.vector_stores)
        self.batches = resources.AsyncBatchesResourceWithStreamingResponse(client.batches)
        self.organization = resources.AsyncOrganizationResourceWithStreamingResponse(client.organization)
        self.projects = resources.AsyncProjectsResourceWithStreamingResponse(client.projects)


Client = Omnistack

AsyncClient = AsyncOmnistack
