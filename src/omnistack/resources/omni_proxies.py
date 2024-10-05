# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import omni_proxy_create_params
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
from .._base_client import make_request_options
from ..types.omni_proxy_create_response import OmniProxyCreateResponse
from ..types.omni_proxy_delete_response import OmniProxyDeleteResponse

__all__ = ["OmniProxiesResource", "AsyncOmniProxiesResource"]


class OmniProxiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OmniProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return OmniProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OmniProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return OmniProxiesResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        omni_model_id: str,
        omniproxy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OmniProxyCreateResponse:
        """
        Add Proxy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/{workspace_id}/proxy/",
            body=maybe_transform(
                {
                    "omni_model_id": omni_model_id,
                    "omniproxy_id": omniproxy_id,
                },
                omni_proxy_create_params.OmniProxyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmniProxyCreateResponse,
        )

    def delete(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OmniProxyDeleteResponse:
        """
        Delete Proxy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not omni_model_id:
            raise ValueError(f"Expected a non-empty value for `omni_model_id` but received {omni_model_id!r}")
        return self._delete(
            f"/{workspace_id}/proxy/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmniProxyDeleteResponse,
        )


class AsyncOmniProxiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOmniProxiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOmniProxiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOmniProxiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncOmniProxiesResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        omni_model_id: str,
        omniproxy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OmniProxyCreateResponse:
        """
        Add Proxy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/{workspace_id}/proxy/",
            body=await async_maybe_transform(
                {
                    "omni_model_id": omni_model_id,
                    "omniproxy_id": omniproxy_id,
                },
                omni_proxy_create_params.OmniProxyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmniProxyCreateResponse,
        )

    async def delete(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OmniProxyDeleteResponse:
        """
        Delete Proxy Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not omni_model_id:
            raise ValueError(f"Expected a non-empty value for `omni_model_id` but received {omni_model_id!r}")
        return await self._delete(
            f"/{workspace_id}/proxy/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OmniProxyDeleteResponse,
        )


class OmniProxiesResourceWithRawResponse:
    def __init__(self, omni_proxies: OmniProxiesResource) -> None:
        self._omni_proxies = omni_proxies

        self.create = to_raw_response_wrapper(
            omni_proxies.create,
        )
        self.delete = to_raw_response_wrapper(
            omni_proxies.delete,
        )


class AsyncOmniProxiesResourceWithRawResponse:
    def __init__(self, omni_proxies: AsyncOmniProxiesResource) -> None:
        self._omni_proxies = omni_proxies

        self.create = async_to_raw_response_wrapper(
            omni_proxies.create,
        )
        self.delete = async_to_raw_response_wrapper(
            omni_proxies.delete,
        )


class OmniProxiesResourceWithStreamingResponse:
    def __init__(self, omni_proxies: OmniProxiesResource) -> None:
        self._omni_proxies = omni_proxies

        self.create = to_streamed_response_wrapper(
            omni_proxies.create,
        )
        self.delete = to_streamed_response_wrapper(
            omni_proxies.delete,
        )


class AsyncOmniProxiesResourceWithStreamingResponse:
    def __init__(self, omni_proxies: AsyncOmniProxiesResource) -> None:
        self._omni_proxies = omni_proxies

        self.create = async_to_streamed_response_wrapper(
            omni_proxies.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            omni_proxies.delete,
        )
