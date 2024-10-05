# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import observability_inference_params
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

__all__ = ["ObservabilityResource", "AsyncObservabilityResource"]


class ObservabilityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObservabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return ObservabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObservabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return ObservabilityResourceWithStreamingResponse(self)

    def inference(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        request_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        observability endpoint for Inference request

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
            f"/{workspace_id}/observability/{omni_model_id}/inference",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "request_type": request_type,
                    },
                    observability_inference_params.ObservabilityInferenceParams,
                ),
            ),
            cast_to=object,
        )


class AsyncObservabilityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObservabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObservabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObservabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncObservabilityResourceWithStreamingResponse(self)

    async def inference(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        request_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        observability endpoint for Inference request

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
            f"/{workspace_id}/observability/{omni_model_id}/inference",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "request_type": request_type,
                    },
                    observability_inference_params.ObservabilityInferenceParams,
                ),
            ),
            cast_to=object,
        )


class ObservabilityResourceWithRawResponse:
    def __init__(self, observability: ObservabilityResource) -> None:
        self._observability = observability

        self.inference = to_raw_response_wrapper(
            observability.inference,
        )


class AsyncObservabilityResourceWithRawResponse:
    def __init__(self, observability: AsyncObservabilityResource) -> None:
        self._observability = observability

        self.inference = async_to_raw_response_wrapper(
            observability.inference,
        )


class ObservabilityResourceWithStreamingResponse:
    def __init__(self, observability: ObservabilityResource) -> None:
        self._observability = observability

        self.inference = to_streamed_response_wrapper(
            observability.inference,
        )


class AsyncObservabilityResourceWithStreamingResponse:
    def __init__(self, observability: AsyncObservabilityResource) -> None:
        self._observability = observability

        self.inference = async_to_streamed_response_wrapper(
            observability.inference,
        )
