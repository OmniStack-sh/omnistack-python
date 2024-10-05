# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .simple import (
    SimpleResource,
    AsyncSimpleResource,
    SimpleResourceWithRawResponse,
    AsyncSimpleResourceWithRawResponse,
    SimpleResourceWithStreamingResponse,
    AsyncSimpleResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def simple(self) -> SimpleResource:
        return SimpleResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def simple(self) -> AsyncSimpleResource:
        return AsyncSimpleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

    @cached_property
    def simple(self) -> SimpleResourceWithRawResponse:
        return SimpleResourceWithRawResponse(self._api_keys.simple)


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

    @cached_property
    def simple(self) -> AsyncSimpleResourceWithRawResponse:
        return AsyncSimpleResourceWithRawResponse(self._api_keys.simple)


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

    @cached_property
    def simple(self) -> SimpleResourceWithStreamingResponse:
        return SimpleResourceWithStreamingResponse(self._api_keys.simple)


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

    @cached_property
    def simple(self) -> AsyncSimpleResourceWithStreamingResponse:
        return AsyncSimpleResourceWithStreamingResponse(self._api_keys.simple)
