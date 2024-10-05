# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import custom_model_deploy_params, custom_model_fetch_custom_model_params
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
from ..types.custom_model_list_response import CustomModelListResponse
from ..types.custom_model_delete_response import CustomModelDeleteResponse
from ..types.custom_model_deploy_response import CustomModelDeployResponse
from ..types.custom_model_retrieve_response import CustomModelRetrieveResponse
from ..types.custom_model_fetch_custom_model_response import CustomModelFetchCustomModelResponse

__all__ = ["CustomModelsResource", "AsyncCustomModelsResource"]


class CustomModelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return CustomModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return CustomModelsResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> CustomModelRetrieveResponse:
        """
        Get Deployment Status

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
        return self._get(
            f"/{workspace_id}/custom_model/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelRetrieveResponse,
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
    ) -> CustomModelListResponse:
        """
        Get Settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/{workspace_id}/custom_model/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelListResponse,
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
    ) -> CustomModelDeleteResponse:
        """
        Delete Deployment

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
            f"/{workspace_id}/custom_model/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelDeleteResponse,
        )

    def deploy(
        self,
        workspace_id: str,
        *,
        gpu_type: str,
        hf_id: str,
        hf_token: str,
        omni_model_id: str,
        active_gpu_worker: int | NotGiven = NOT_GIVEN,
        execution_timeout: int | NotGiven = NOT_GIVEN,
        gpu_idle_timeout: int | NotGiven = NOT_GIVEN,
        max_gpu_worker: int | NotGiven = NOT_GIVEN,
        scale_type: Literal["QUEUE_DELAY", "REQUEST_COUNT"] | NotGiven = NOT_GIVEN,
        scaler_value: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomModelDeployResponse:
        """
        Deploy Custom Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/{workspace_id}/custom_model/deploy",
            body=maybe_transform(
                {
                    "gpu_type": gpu_type,
                    "hf_id": hf_id,
                    "hf_token": hf_token,
                    "omni_model_id": omni_model_id,
                    "active_gpu_worker": active_gpu_worker,
                    "execution_timeout": execution_timeout,
                    "gpu_idle_timeout": gpu_idle_timeout,
                    "max_gpu_worker": max_gpu_worker,
                    "scale_type": scale_type,
                    "scaler_value": scaler_value,
                },
                custom_model_deploy_params.CustomModelDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelDeployResponse,
        )

    def fetch_custom_model(
        self,
        workspace_id: str,
        *,
        hf_id: str,
        hf_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomModelFetchCustomModelResponse:
        """
        Fetch custom model setup

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/{workspace_id}/custom_model/fetch_custom_model",
            body=maybe_transform(
                {
                    "hf_id": hf_id,
                    "hf_token": hf_token,
                },
                custom_model_fetch_custom_model_params.CustomModelFetchCustomModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelFetchCustomModelResponse,
        )


class AsyncCustomModelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncCustomModelsResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> CustomModelRetrieveResponse:
        """
        Get Deployment Status

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
        return await self._get(
            f"/{workspace_id}/custom_model/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelRetrieveResponse,
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
    ) -> CustomModelListResponse:
        """
        Get Settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/{workspace_id}/custom_model/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelListResponse,
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
    ) -> CustomModelDeleteResponse:
        """
        Delete Deployment

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
            f"/{workspace_id}/custom_model/{omni_model_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelDeleteResponse,
        )

    async def deploy(
        self,
        workspace_id: str,
        *,
        gpu_type: str,
        hf_id: str,
        hf_token: str,
        omni_model_id: str,
        active_gpu_worker: int | NotGiven = NOT_GIVEN,
        execution_timeout: int | NotGiven = NOT_GIVEN,
        gpu_idle_timeout: int | NotGiven = NOT_GIVEN,
        max_gpu_worker: int | NotGiven = NOT_GIVEN,
        scale_type: Literal["QUEUE_DELAY", "REQUEST_COUNT"] | NotGiven = NOT_GIVEN,
        scaler_value: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomModelDeployResponse:
        """
        Deploy Custom Model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/{workspace_id}/custom_model/deploy",
            body=await async_maybe_transform(
                {
                    "gpu_type": gpu_type,
                    "hf_id": hf_id,
                    "hf_token": hf_token,
                    "omni_model_id": omni_model_id,
                    "active_gpu_worker": active_gpu_worker,
                    "execution_timeout": execution_timeout,
                    "gpu_idle_timeout": gpu_idle_timeout,
                    "max_gpu_worker": max_gpu_worker,
                    "scale_type": scale_type,
                    "scaler_value": scaler_value,
                },
                custom_model_deploy_params.CustomModelDeployParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelDeployResponse,
        )

    async def fetch_custom_model(
        self,
        workspace_id: str,
        *,
        hf_id: str,
        hf_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomModelFetchCustomModelResponse:
        """
        Fetch custom model setup

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/{workspace_id}/custom_model/fetch_custom_model",
            body=await async_maybe_transform(
                {
                    "hf_id": hf_id,
                    "hf_token": hf_token,
                },
                custom_model_fetch_custom_model_params.CustomModelFetchCustomModelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomModelFetchCustomModelResponse,
        )


class CustomModelsResourceWithRawResponse:
    def __init__(self, custom_models: CustomModelsResource) -> None:
        self._custom_models = custom_models

        self.retrieve = to_raw_response_wrapper(
            custom_models.retrieve,
        )
        self.list = to_raw_response_wrapper(
            custom_models.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_models.delete,
        )
        self.deploy = to_raw_response_wrapper(
            custom_models.deploy,
        )
        self.fetch_custom_model = to_raw_response_wrapper(
            custom_models.fetch_custom_model,
        )


class AsyncCustomModelsResourceWithRawResponse:
    def __init__(self, custom_models: AsyncCustomModelsResource) -> None:
        self._custom_models = custom_models

        self.retrieve = async_to_raw_response_wrapper(
            custom_models.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            custom_models.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_models.delete,
        )
        self.deploy = async_to_raw_response_wrapper(
            custom_models.deploy,
        )
        self.fetch_custom_model = async_to_raw_response_wrapper(
            custom_models.fetch_custom_model,
        )


class CustomModelsResourceWithStreamingResponse:
    def __init__(self, custom_models: CustomModelsResource) -> None:
        self._custom_models = custom_models

        self.retrieve = to_streamed_response_wrapper(
            custom_models.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            custom_models.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_models.delete,
        )
        self.deploy = to_streamed_response_wrapper(
            custom_models.deploy,
        )
        self.fetch_custom_model = to_streamed_response_wrapper(
            custom_models.fetch_custom_model,
        )


class AsyncCustomModelsResourceWithStreamingResponse:
    def __init__(self, custom_models: AsyncCustomModelsResource) -> None:
        self._custom_models = custom_models

        self.retrieve = async_to_streamed_response_wrapper(
            custom_models.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_models.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_models.delete,
        )
        self.deploy = async_to_streamed_response_wrapper(
            custom_models.deploy,
        )
        self.fetch_custom_model = async_to_streamed_response_wrapper(
            custom_models.fetch_custom_model,
        )
