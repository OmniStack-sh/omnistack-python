# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime

import httpx

from ..types import (
    models_dashboard_overview_request_params,
    models_dashboard_overview_basic_stats_params,
    models_dashboard_overview_cost_per_request_params,
    models_dashboard_overview_tokens_per_request_params,
    models_dashboard_overview_latency_per_request_params,
    models_dashboard_overview_time_to_first_token_params,
    models_dashboard_overview_request_country_distribution_params,
)
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
from ..types.basic_stats import BasicStats
from ..types.request_data import RequestData
from ..types.tokens_per_request import TokensPerRequest
from ..types.time_to_first_token import TimeToFirstToken
from ..types.request_country_distribution import RequestCountryDistribution
from ..types.models_dashboard_overview_retrieve_response import ModelsDashboardOverviewRetrieveResponse
from ..types.models_dashboard_overview_cost_per_request_response import ModelsDashboardOverviewCostPerRequestResponse
from ..types.models_dashboard_overview_latency_per_request_response import (
    ModelsDashboardOverviewLatencyPerRequestResponse,
)

__all__ = ["ModelsDashboardOverviewResource", "AsyncModelsDashboardOverviewResource"]


class ModelsDashboardOverviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelsDashboardOverviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return ModelsDashboardOverviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsDashboardOverviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return ModelsDashboardOverviewResourceWithStreamingResponse(self)

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
    ) -> ModelsDashboardOverviewRetrieveResponse:
        """
        Get Model Status

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
        return cast(
            ModelsDashboardOverviewRetrieveResponse,
            self._get(
                f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelsDashboardOverviewRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def basic_stats(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicStats:
        """
        Get Total Cost

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
        return self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/basic_stats",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_basic_stats_params.ModelsDashboardOverviewBasicStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicStats,
        )

    def cost_per_request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelsDashboardOverviewCostPerRequestResponse:
        """
        Get Cost Per Request

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
        return cast(
            ModelsDashboardOverviewCostPerRequestResponse,
            self._post(
                f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/cost_per_request",
                body=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    models_dashboard_overview_cost_per_request_params.ModelsDashboardOverviewCostPerRequestParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelsDashboardOverviewCostPerRequestResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def latency_per_request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelsDashboardOverviewLatencyPerRequestResponse:
        """
        Get Latency Per Request

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
        return cast(
            ModelsDashboardOverviewLatencyPerRequestResponse,
            self._post(
                f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/latency_per_request",
                body=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    models_dashboard_overview_latency_per_request_params.ModelsDashboardOverviewLatencyPerRequestParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelsDashboardOverviewLatencyPerRequestResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestData:
        """
        Get Request Data

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
        return self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/request",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_request_params.ModelsDashboardOverviewRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestData,
        )

    def request_country_distribution(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestCountryDistribution:
        """
        Get Request Country Distribution

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
        return self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/request_country_distribution",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_request_country_distribution_params.ModelsDashboardOverviewRequestCountryDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestCountryDistribution,
        )

    def time_to_first_token(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeToFirstToken:
        """
        Get Time To First Token

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
        return self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/time_to_first_token",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_time_to_first_token_params.ModelsDashboardOverviewTimeToFirstTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeToFirstToken,
        )

    def tokens_per_request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokensPerRequest:
        """
        Get Tokens Per Request

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
        return self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/tokens_per_request",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_tokens_per_request_params.ModelsDashboardOverviewTokensPerRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokensPerRequest,
        )


class AsyncModelsDashboardOverviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelsDashboardOverviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsDashboardOverviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsDashboardOverviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/omnistack-python#with_streaming_response
        """
        return AsyncModelsDashboardOverviewResourceWithStreamingResponse(self)

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
    ) -> ModelsDashboardOverviewRetrieveResponse:
        """
        Get Model Status

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
        return cast(
            ModelsDashboardOverviewRetrieveResponse,
            await self._get(
                f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelsDashboardOverviewRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def basic_stats(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BasicStats:
        """
        Get Total Cost

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
        return await self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/basic_stats",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_basic_stats_params.ModelsDashboardOverviewBasicStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BasicStats,
        )

    async def cost_per_request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelsDashboardOverviewCostPerRequestResponse:
        """
        Get Cost Per Request

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
        return cast(
            ModelsDashboardOverviewCostPerRequestResponse,
            await self._post(
                f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/cost_per_request",
                body=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    models_dashboard_overview_cost_per_request_params.ModelsDashboardOverviewCostPerRequestParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelsDashboardOverviewCostPerRequestResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def latency_per_request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelsDashboardOverviewLatencyPerRequestResponse:
        """
        Get Latency Per Request

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
        return cast(
            ModelsDashboardOverviewLatencyPerRequestResponse,
            await self._post(
                f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/latency_per_request",
                body=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    models_dashboard_overview_latency_per_request_params.ModelsDashboardOverviewLatencyPerRequestParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ModelsDashboardOverviewLatencyPerRequestResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestData:
        """
        Get Request Data

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
        return await self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/request",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_request_params.ModelsDashboardOverviewRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestData,
        )

    async def request_country_distribution(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestCountryDistribution:
        """
        Get Request Country Distribution

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
        return await self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/request_country_distribution",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_request_country_distribution_params.ModelsDashboardOverviewRequestCountryDistributionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestCountryDistribution,
        )

    async def time_to_first_token(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeToFirstToken:
        """
        Get Time To First Token

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
        return await self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/time_to_first_token",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_time_to_first_token_params.ModelsDashboardOverviewTimeToFirstTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeToFirstToken,
        )

    async def tokens_per_request(
        self,
        omni_model_id: str,
        *,
        workspace_id: str,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokensPerRequest:
        """
        Get Tokens Per Request

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
        return await self._post(
            f"/{workspace_id}/models/dashboard/{omni_model_id}/overview/tokens_per_request",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                models_dashboard_overview_tokens_per_request_params.ModelsDashboardOverviewTokensPerRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokensPerRequest,
        )


class ModelsDashboardOverviewResourceWithRawResponse:
    def __init__(self, models_dashboard_overview: ModelsDashboardOverviewResource) -> None:
        self._models_dashboard_overview = models_dashboard_overview

        self.retrieve = to_raw_response_wrapper(
            models_dashboard_overview.retrieve,
        )
        self.basic_stats = to_raw_response_wrapper(
            models_dashboard_overview.basic_stats,
        )
        self.cost_per_request = to_raw_response_wrapper(
            models_dashboard_overview.cost_per_request,
        )
        self.latency_per_request = to_raw_response_wrapper(
            models_dashboard_overview.latency_per_request,
        )
        self.request = to_raw_response_wrapper(
            models_dashboard_overview.request,
        )
        self.request_country_distribution = to_raw_response_wrapper(
            models_dashboard_overview.request_country_distribution,
        )
        self.time_to_first_token = to_raw_response_wrapper(
            models_dashboard_overview.time_to_first_token,
        )
        self.tokens_per_request = to_raw_response_wrapper(
            models_dashboard_overview.tokens_per_request,
        )


class AsyncModelsDashboardOverviewResourceWithRawResponse:
    def __init__(self, models_dashboard_overview: AsyncModelsDashboardOverviewResource) -> None:
        self._models_dashboard_overview = models_dashboard_overview

        self.retrieve = async_to_raw_response_wrapper(
            models_dashboard_overview.retrieve,
        )
        self.basic_stats = async_to_raw_response_wrapper(
            models_dashboard_overview.basic_stats,
        )
        self.cost_per_request = async_to_raw_response_wrapper(
            models_dashboard_overview.cost_per_request,
        )
        self.latency_per_request = async_to_raw_response_wrapper(
            models_dashboard_overview.latency_per_request,
        )
        self.request = async_to_raw_response_wrapper(
            models_dashboard_overview.request,
        )
        self.request_country_distribution = async_to_raw_response_wrapper(
            models_dashboard_overview.request_country_distribution,
        )
        self.time_to_first_token = async_to_raw_response_wrapper(
            models_dashboard_overview.time_to_first_token,
        )
        self.tokens_per_request = async_to_raw_response_wrapper(
            models_dashboard_overview.tokens_per_request,
        )


class ModelsDashboardOverviewResourceWithStreamingResponse:
    def __init__(self, models_dashboard_overview: ModelsDashboardOverviewResource) -> None:
        self._models_dashboard_overview = models_dashboard_overview

        self.retrieve = to_streamed_response_wrapper(
            models_dashboard_overview.retrieve,
        )
        self.basic_stats = to_streamed_response_wrapper(
            models_dashboard_overview.basic_stats,
        )
        self.cost_per_request = to_streamed_response_wrapper(
            models_dashboard_overview.cost_per_request,
        )
        self.latency_per_request = to_streamed_response_wrapper(
            models_dashboard_overview.latency_per_request,
        )
        self.request = to_streamed_response_wrapper(
            models_dashboard_overview.request,
        )
        self.request_country_distribution = to_streamed_response_wrapper(
            models_dashboard_overview.request_country_distribution,
        )
        self.time_to_first_token = to_streamed_response_wrapper(
            models_dashboard_overview.time_to_first_token,
        )
        self.tokens_per_request = to_streamed_response_wrapper(
            models_dashboard_overview.tokens_per_request,
        )


class AsyncModelsDashboardOverviewResourceWithStreamingResponse:
    def __init__(self, models_dashboard_overview: AsyncModelsDashboardOverviewResource) -> None:
        self._models_dashboard_overview = models_dashboard_overview

        self.retrieve = async_to_streamed_response_wrapper(
            models_dashboard_overview.retrieve,
        )
        self.basic_stats = async_to_streamed_response_wrapper(
            models_dashboard_overview.basic_stats,
        )
        self.cost_per_request = async_to_streamed_response_wrapper(
            models_dashboard_overview.cost_per_request,
        )
        self.latency_per_request = async_to_streamed_response_wrapper(
            models_dashboard_overview.latency_per_request,
        )
        self.request = async_to_streamed_response_wrapper(
            models_dashboard_overview.request,
        )
        self.request_country_distribution = async_to_streamed_response_wrapper(
            models_dashboard_overview.request_country_distribution,
        )
        self.time_to_first_token = async_to_streamed_response_wrapper(
            models_dashboard_overview.time_to_first_token,
        )
        self.tokens_per_request = async_to_streamed_response_wrapper(
            models_dashboard_overview.tokens_per_request,
        )
