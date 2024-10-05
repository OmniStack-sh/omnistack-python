# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .external import (
    ExternalResource,
    AsyncExternalResource,
    ExternalResourceWithRawResponse,
    AsyncExternalResourceWithRawResponse,
    ExternalResourceWithStreamingResponse,
    AsyncExternalResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EvalsResource", "AsyncEvalsResource"]


class EvalsResource(SyncAPIResource):
    @cached_property
    def external(self) -> ExternalResource:
        return ExternalResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return EvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return EvalsResourceWithStreamingResponse(self)


class AsyncEvalsResource(AsyncAPIResource):
    @cached_property
    def external(self) -> AsyncExternalResource:
        return AsyncExternalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncEvalsResourceWithStreamingResponse(self)


class EvalsResourceWithRawResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

    @cached_property
    def external(self) -> ExternalResourceWithRawResponse:
        return ExternalResourceWithRawResponse(self._evals.external)


class AsyncEvalsResourceWithRawResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

    @cached_property
    def external(self) -> AsyncExternalResourceWithRawResponse:
        return AsyncExternalResourceWithRawResponse(self._evals.external)


class EvalsResourceWithStreamingResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

    @cached_property
    def external(self) -> ExternalResourceWithStreamingResponse:
        return ExternalResourceWithStreamingResponse(self._evals.external)


class AsyncEvalsResourceWithStreamingResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

    @cached_property
    def external(self) -> AsyncExternalResourceWithStreamingResponse:
        return AsyncExternalResourceWithStreamingResponse(self._evals.external)
