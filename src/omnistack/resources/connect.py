# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import connect_list_params, connect_deploy_params, connect_fetch_external_provider_params
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
from ..types.connect_list_response import ConnectListResponse
from ..types.connect_delete_response import ConnectDeleteResponse
from ..types.connect_deploy_response import ConnectDeployResponse
from ..types.connect_fetch_external_provider_response import ConnectFetchExternalProviderResponse

__all__ = ["ConnectResource", "AsyncConnectResource"]


class ConnectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return ConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return ConnectResourceWithStreamingResponse(self)

    def list(
        self,
        workspace_id: str,
        *,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectListResponse:
        """
        Get Providers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/{workspace_id}/connect/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"provider_id": provider_id}, connect_list_params.ConnectListParams),
            ),
            cast_to=ConnectListResponse,
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
    ) -> ConnectDeleteResponse:
        """
        Delete External Model

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
            f"/{workspace_id}/connect/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectDeleteResponse,
        )

    def deploy(
        self,
        workspace_id: str,
        *,
        model_provider: Literal["openai", "groq"],
        omni_model_id: str,
        provide_model_id: str,
        provider_api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectDeployResponse:
        """
        Test the model and add to user's workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/{workspace_id}/connect/deploy",
            body=maybe_transform(
                {
                    "model_provider": model_provider,
                    "omni_model_id": omni_model_id,
                    "provide_model_id": provide_model_id,
                    "provider_api_key": provider_api_key,
                },
                connect_deploy_params.ConnectDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectDeployResponse,
        )

    def fetch_external_provider(
        self,
        workspace_id: str,
        *,
        model_provider: Literal["openai", "groq", "claudi"],
        provider_api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectFetchExternalProviderResponse:
        """
        Test the api key and return the list of available models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/{workspace_id}/connect/fetch_external_provider",
            body=maybe_transform(
                {
                    "model_provider": model_provider,
                    "provider_api_key": provider_api_key,
                },
                connect_fetch_external_provider_params.ConnectFetchExternalProviderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectFetchExternalProviderResponse,
        )


class AsyncConnectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncConnectResourceWithStreamingResponse(self)

    async def list(
        self,
        workspace_id: str,
        *,
        provider_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectListResponse:
        """
        Get Providers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/{workspace_id}/connect/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"provider_id": provider_id}, connect_list_params.ConnectListParams),
            ),
            cast_to=ConnectListResponse,
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
    ) -> ConnectDeleteResponse:
        """
        Delete External Model

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
            f"/{workspace_id}/connect/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectDeleteResponse,
        )

    async def deploy(
        self,
        workspace_id: str,
        *,
        model_provider: Literal["openai", "groq"],
        omni_model_id: str,
        provide_model_id: str,
        provider_api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectDeployResponse:
        """
        Test the model and add to user's workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/{workspace_id}/connect/deploy",
            body=await async_maybe_transform(
                {
                    "model_provider": model_provider,
                    "omni_model_id": omni_model_id,
                    "provide_model_id": provide_model_id,
                    "provider_api_key": provider_api_key,
                },
                connect_deploy_params.ConnectDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectDeployResponse,
        )

    async def fetch_external_provider(
        self,
        workspace_id: str,
        *,
        model_provider: Literal["openai", "groq", "claudi"],
        provider_api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectFetchExternalProviderResponse:
        """
        Test the api key and return the list of available models

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/{workspace_id}/connect/fetch_external_provider",
            body=await async_maybe_transform(
                {
                    "model_provider": model_provider,
                    "provider_api_key": provider_api_key,
                },
                connect_fetch_external_provider_params.ConnectFetchExternalProviderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectFetchExternalProviderResponse,
        )


class ConnectResourceWithRawResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.list = to_raw_response_wrapper(
            connect.list,
        )
        self.delete = to_raw_response_wrapper(
            connect.delete,
        )
        self.deploy = to_raw_response_wrapper(
            connect.deploy,
        )
        self.fetch_external_provider = to_raw_response_wrapper(
            connect.fetch_external_provider,
        )


class AsyncConnectResourceWithRawResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.list = async_to_raw_response_wrapper(
            connect.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connect.delete,
        )
        self.deploy = async_to_raw_response_wrapper(
            connect.deploy,
        )
        self.fetch_external_provider = async_to_raw_response_wrapper(
            connect.fetch_external_provider,
        )


class ConnectResourceWithStreamingResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.list = to_streamed_response_wrapper(
            connect.list,
        )
        self.delete = to_streamed_response_wrapper(
            connect.delete,
        )
        self.deploy = to_streamed_response_wrapper(
            connect.deploy,
        )
        self.fetch_external_provider = to_streamed_response_wrapper(
            connect.fetch_external_provider,
        )


class AsyncConnectResourceWithStreamingResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.list = async_to_streamed_response_wrapper(
            connect.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connect.delete,
        )
        self.deploy = async_to_streamed_response_wrapper(
            connect.deploy,
        )
        self.fetch_external_provider = async_to_streamed_response_wrapper(
            connect.fetch_external_provider,
        )
