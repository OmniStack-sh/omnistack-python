# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import ExploreModelResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExplore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Omnistack) -> None:
        explore = client.explore.list(
            "workspace_id",
        )
        assert_matches_type(ExploreModelResponse, explore, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Omnistack) -> None:
        response = client.explore.with_raw_response.list(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explore = response.parse()
        assert_matches_type(ExploreModelResponse, explore, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Omnistack) -> None:
        with client.explore.with_streaming_response.list(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explore = response.parse()
            assert_matches_type(ExploreModelResponse, explore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.explore.with_raw_response.list(
                "",
            )


class TestAsyncExplore:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOmnistack) -> None:
        explore = await async_client.explore.list(
            "workspace_id",
        )
        assert_matches_type(ExploreModelResponse, explore, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.explore.with_raw_response.list(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explore = await response.parse()
        assert_matches_type(ExploreModelResponse, explore, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOmnistack) -> None:
        async with async_client.explore.with_streaming_response.list(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explore = await response.parse()
            assert_matches_type(ExploreModelResponse, explore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.explore.with_raw_response.list(
                "",
            )
