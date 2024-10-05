# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["PlaygroundResource", "AsyncPlaygroundResource"]


class PlaygroundResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlaygroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return PlaygroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaygroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return PlaygroundResourceWithStreamingResponse(self)

    def retrieve(
        self,
        project_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Playground

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/{workspace_id}/projects/{project_id}/playground/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPlaygroundResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlaygroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaygroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaygroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncPlaygroundResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        project_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get Playground

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/{workspace_id}/projects/{project_id}/playground/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PlaygroundResourceWithRawResponse:
    def __init__(self, playground: PlaygroundResource) -> None:
        self._playground = playground

        self.retrieve = to_raw_response_wrapper(
            playground.retrieve,
        )


class AsyncPlaygroundResourceWithRawResponse:
    def __init__(self, playground: AsyncPlaygroundResource) -> None:
        self._playground = playground

        self.retrieve = async_to_raw_response_wrapper(
            playground.retrieve,
        )


class PlaygroundResourceWithStreamingResponse:
    def __init__(self, playground: PlaygroundResource) -> None:
        self._playground = playground

        self.retrieve = to_streamed_response_wrapper(
            playground.retrieve,
        )


class AsyncPlaygroundResourceWithStreamingResponse:
    def __init__(self, playground: AsyncPlaygroundResource) -> None:
        self._playground = playground

        self.retrieve = async_to_streamed_response_wrapper(
            playground.retrieve,
        )
