# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workspaces.api_keys import simple_create_params
from ....types.workspaces.api_keys.simple_list_response import SimpleListResponse
from ....types.workspaces.api_keys.simple_create_response import SimpleCreateResponse
from ....types.workspaces.api_keys.simple_delete_response import SimpleDeleteResponse

__all__ = ["SimpleResource", "AsyncSimpleResource"]


class SimpleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return SimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return SimpleResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        access_type: Literal["MODEL", "PLATFORM"],
        api_key_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleCreateResponse:
        """
        Create Simple API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/{workspace_id}/apikey/simple/create",
            body=maybe_transform(
                {
                    "access_type": access_type,
                    "api_key_name": api_key_name,
                },
                simple_create_params.SimpleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleCreateResponse,
        )

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
    ) -> SimpleListResponse:
        """
        Get Simple API keys

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/{workspace_id}/apikey/simple/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleListResponse,
        )

    def delete(
        self,
        api_key_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleDeleteResponse:
        """
        Delete Simple API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return self._delete(
            f"/{workspace_id}/apikey/simple/{api_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleDeleteResponse,
        )


class AsyncSimpleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncSimpleResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        access_type: Literal["MODEL", "PLATFORM"],
        api_key_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleCreateResponse:
        """
        Create Simple API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/{workspace_id}/apikey/simple/create",
            body=await async_maybe_transform(
                {
                    "access_type": access_type,
                    "api_key_name": api_key_name,
                },
                simple_create_params.SimpleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleCreateResponse,
        )

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
    ) -> SimpleListResponse:
        """
        Get Simple API keys

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/{workspace_id}/apikey/simple/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleListResponse,
        )

    async def delete(
        self,
        api_key_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleDeleteResponse:
        """
        Delete Simple API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not api_key_id:
            raise ValueError(f"Expected a non-empty value for `api_key_id` but received {api_key_id!r}")
        return await self._delete(
            f"/{workspace_id}/apikey/simple/{api_key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleDeleteResponse,
        )


class SimpleResourceWithRawResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

        self.create = to_raw_response_wrapper(
            simple.create,
        )
        self.list = to_raw_response_wrapper(
            simple.list,
        )
        self.delete = to_raw_response_wrapper(
            simple.delete,
        )


class AsyncSimpleResourceWithRawResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

        self.create = async_to_raw_response_wrapper(
            simple.create,
        )
        self.list = async_to_raw_response_wrapper(
            simple.list,
        )
        self.delete = async_to_raw_response_wrapper(
            simple.delete,
        )


class SimpleResourceWithStreamingResponse:
    def __init__(self, simple: SimpleResource) -> None:
        self._simple = simple

        self.create = to_streamed_response_wrapper(
            simple.create,
        )
        self.list = to_streamed_response_wrapper(
            simple.list,
        )
        self.delete = to_streamed_response_wrapper(
            simple.delete,
        )


class AsyncSimpleResourceWithStreamingResponse:
    def __init__(self, simple: AsyncSimpleResource) -> None:
        self._simple = simple

        self.create = async_to_streamed_response_wrapper(
            simple.create,
        )
        self.list = async_to_streamed_response_wrapper(
            simple.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            simple.delete,
        )
