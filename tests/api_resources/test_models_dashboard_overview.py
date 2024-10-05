# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import (
    BasicStats,
    RequestData,
    TimeToFirstToken,
    TokensPerRequest,
    RequestCountryDistribution,
    ModelsDashboardOverviewRetrieveResponse,
    ModelsDashboardOverviewCostPerRequestResponse,
    ModelsDashboardOverviewLatencyPerRequestResponse,
)
from omnistack._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModelsDashboardOverview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(ModelsDashboardOverviewRetrieveResponse, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(ModelsDashboardOverviewRetrieveResponse, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(ModelsDashboardOverviewRetrieveResponse, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.retrieve(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.retrieve(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_basic_stats(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.basic_stats(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(BasicStats, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_basic_stats(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.basic_stats(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(BasicStats, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_basic_stats(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.basic_stats(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(BasicStats, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_basic_stats(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.basic_stats(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.basic_stats(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    def test_method_cost_per_request(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.cost_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(ModelsDashboardOverviewCostPerRequestResponse, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_cost_per_request(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.cost_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(ModelsDashboardOverviewCostPerRequestResponse, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_cost_per_request(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.cost_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(
                ModelsDashboardOverviewCostPerRequestResponse, models_dashboard_overview, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cost_per_request(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.cost_per_request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.cost_per_request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    def test_method_latency_per_request(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.latency_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(
            ModelsDashboardOverviewLatencyPerRequestResponse, models_dashboard_overview, path=["response"]
        )

    @parametrize
    def test_raw_response_latency_per_request(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.latency_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(
            ModelsDashboardOverviewLatencyPerRequestResponse, models_dashboard_overview, path=["response"]
        )

    @parametrize
    def test_streaming_response_latency_per_request(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.latency_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(
                ModelsDashboardOverviewLatencyPerRequestResponse, models_dashboard_overview, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_latency_per_request(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.latency_per_request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.latency_per_request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    def test_method_request(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(RequestData, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_request(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(RequestData, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_request(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(RequestData, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_request(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    def test_method_request_country_distribution(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.request_country_distribution(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(RequestCountryDistribution, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_request_country_distribution(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.request_country_distribution(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(RequestCountryDistribution, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_request_country_distribution(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.request_country_distribution(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(RequestCountryDistribution, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_request_country_distribution(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.request_country_distribution(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.request_country_distribution(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    def test_method_time_to_first_token(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.time_to_first_token(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(TimeToFirstToken, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_time_to_first_token(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.time_to_first_token(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(TimeToFirstToken, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_time_to_first_token(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.time_to_first_token(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(TimeToFirstToken, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_time_to_first_token(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.time_to_first_token(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.time_to_first_token(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    def test_method_tokens_per_request(self, client: Omnistack) -> None:
        models_dashboard_overview = client.models_dashboard_overview.tokens_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(TokensPerRequest, models_dashboard_overview, path=["response"])

    @parametrize
    def test_raw_response_tokens_per_request(self, client: Omnistack) -> None:
        response = client.models_dashboard_overview.with_raw_response.tokens_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = response.parse()
        assert_matches_type(TokensPerRequest, models_dashboard_overview, path=["response"])

    @parametrize
    def test_streaming_response_tokens_per_request(self, client: Omnistack) -> None:
        with client.models_dashboard_overview.with_streaming_response.tokens_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = response.parse()
            assert_matches_type(TokensPerRequest, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tokens_per_request(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.tokens_per_request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.models_dashboard_overview.with_raw_response.tokens_per_request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )


class TestAsyncModelsDashboardOverview:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(ModelsDashboardOverviewRetrieveResponse, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(ModelsDashboardOverviewRetrieveResponse, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(ModelsDashboardOverviewRetrieveResponse, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.retrieve(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.retrieve(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_basic_stats(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.basic_stats(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(BasicStats, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_basic_stats(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.basic_stats(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(BasicStats, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_basic_stats(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.basic_stats(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(BasicStats, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_basic_stats(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.basic_stats(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.basic_stats(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    async def test_method_cost_per_request(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.cost_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(ModelsDashboardOverviewCostPerRequestResponse, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_cost_per_request(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.cost_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(ModelsDashboardOverviewCostPerRequestResponse, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_cost_per_request(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.cost_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(
                ModelsDashboardOverviewCostPerRequestResponse, models_dashboard_overview, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cost_per_request(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.cost_per_request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.cost_per_request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    async def test_method_latency_per_request(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.latency_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(
            ModelsDashboardOverviewLatencyPerRequestResponse, models_dashboard_overview, path=["response"]
        )

    @parametrize
    async def test_raw_response_latency_per_request(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.latency_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(
            ModelsDashboardOverviewLatencyPerRequestResponse, models_dashboard_overview, path=["response"]
        )

    @parametrize
    async def test_streaming_response_latency_per_request(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.latency_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(
                ModelsDashboardOverviewLatencyPerRequestResponse, models_dashboard_overview, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_latency_per_request(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.latency_per_request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.latency_per_request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    async def test_method_request(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(RequestData, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_request(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(RequestData, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_request(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(RequestData, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_request(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    async def test_method_request_country_distribution(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.request_country_distribution(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(RequestCountryDistribution, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_request_country_distribution(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.request_country_distribution(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(RequestCountryDistribution, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_request_country_distribution(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.request_country_distribution(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(RequestCountryDistribution, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_request_country_distribution(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.request_country_distribution(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.request_country_distribution(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    async def test_method_time_to_first_token(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.time_to_first_token(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(TimeToFirstToken, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_time_to_first_token(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.time_to_first_token(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(TimeToFirstToken, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_time_to_first_token(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.time_to_first_token(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(TimeToFirstToken, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_time_to_first_token(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.time_to_first_token(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.time_to_first_token(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

    @parametrize
    async def test_method_tokens_per_request(self, async_client: AsyncOmnistack) -> None:
        models_dashboard_overview = await async_client.models_dashboard_overview.tokens_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )
        assert_matches_type(TokensPerRequest, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_raw_response_tokens_per_request(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.models_dashboard_overview.with_raw_response.tokens_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_dashboard_overview = await response.parse()
        assert_matches_type(TokensPerRequest, models_dashboard_overview, path=["response"])

    @parametrize
    async def test_streaming_response_tokens_per_request(self, async_client: AsyncOmnistack) -> None:
        async with async_client.models_dashboard_overview.with_streaming_response.tokens_per_request(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
            start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_dashboard_overview = await response.parse()
            assert_matches_type(TokensPerRequest, models_dashboard_overview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tokens_per_request(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.tokens_per_request(
                omni_model_id="omni_model_id",
                workspace_id="",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.models_dashboard_overview.with_raw_response.tokens_per_request(
                omni_model_id="",
                workspace_id="workspace_id",
                end_date=parse_datetime("2024-10-04T17:37:14.830761Z"),
                start_date=parse_datetime("2024-09-27T17:37:14.830754Z"),
            )
