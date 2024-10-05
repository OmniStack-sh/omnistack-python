# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import proxy_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.proxy import Proxy
from .._base_client import make_request_options

__all__ = ["ProxiesResource", "AsyncProxiesResource"]


class ProxiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return ProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return ProxiesResourceWithStreamingResponse(self)

    def list(
        self,
        workspace_id: str,
        *,
        omniproxy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Proxy:
        """
        Get Proxy Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/{workspace_id}/proxy/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"omniproxy_id": omniproxy_id}, proxy_list_params.ProxyListParams),
            ),
            cast_to=Proxy,
        )


class AsyncProxiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncProxiesResourceWithStreamingResponse(self)

    async def list(
        self,
        workspace_id: str,
        *,
        omniproxy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Proxy:
        """
        Get Proxy Models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/{workspace_id}/proxy/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"omniproxy_id": omniproxy_id}, proxy_list_params.ProxyListParams),
            ),
            cast_to=Proxy,
        )


class ProxiesResourceWithRawResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.list = to_raw_response_wrapper(
            proxies.list,
        )


class AsyncProxiesResourceWithRawResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.list = async_to_raw_response_wrapper(
            proxies.list,
        )


class ProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: ProxiesResource) -> None:
        self._proxies = proxies

        self.list = to_streamed_response_wrapper(
            proxies.list,
        )


class AsyncProxiesResourceWithStreamingResponse:
    def __init__(self, proxies: AsyncProxiesResource) -> None:
        self._proxies = proxies

        self.list = async_to_streamed_response_wrapper(
            proxies.list,
        )
