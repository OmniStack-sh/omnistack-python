# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.explore_model_response import ExploreModelResponse

__all__ = ["ExploreResource", "AsyncExploreResource"]


class ExploreResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExploreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return ExploreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExploreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return ExploreResourceWithStreamingResponse(self)

    def list(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExploreModelResponse:
        """
        Explore Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/{workspace_id}/models/explore/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExploreModelResponse,
        )


class AsyncExploreResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExploreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExploreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExploreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncExploreResourceWithStreamingResponse(self)

    async def list(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExploreModelResponse:
        """
        Explore Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/{workspace_id}/models/explore/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExploreModelResponse,
        )


class ExploreResourceWithRawResponse:
    def __init__(self, explore: ExploreResource) -> None:
        self._explore = explore

        self.list = to_raw_response_wrapper(
            explore.list,
        )


class AsyncExploreResourceWithRawResponse:
    def __init__(self, explore: AsyncExploreResource) -> None:
        self._explore = explore

        self.list = async_to_raw_response_wrapper(
            explore.list,
        )


class ExploreResourceWithStreamingResponse:
    def __init__(self, explore: ExploreResource) -> None:
        self._explore = explore

        self.list = to_streamed_response_wrapper(
            explore.list,
        )


class AsyncExploreResourceWithStreamingResponse:
    def __init__(self, explore: AsyncExploreResource) -> None:
        self._explore = explore

        self.list = async_to_streamed_response_wrapper(
            explore.list,
        )
