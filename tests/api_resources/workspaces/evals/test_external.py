# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Omnistack) -> None:
        external = client.workspaces.evals.external.create(
            workspace_id="workspace_id",
            eval_id="eval_id",
            eval_type="external",
            omni_model_id="omni_model_id",
        )
        assert_matches_type(object, external, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Omnistack) -> None:
        response = client.workspaces.evals.external.with_raw_response.create(
            workspace_id="workspace_id",
            eval_id="eval_id",
            eval_type="external",
            omni_model_id="omni_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = response.parse()
        assert_matches_type(object, external, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Omnistack) -> None:
        with client.workspaces.evals.external.with_streaming_response.create(
            workspace_id="workspace_id",
            eval_id="eval_id",
            eval_type="external",
            omni_model_id="omni_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = response.parse()
            assert_matches_type(object, external, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.evals.external.with_raw_response.create(
                workspace_id="",
                eval_id="eval_id",
                eval_type="external",
                omni_model_id="omni_model_id",
            )


class TestAsyncExternal:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOmnistack) -> None:
        external = await async_client.workspaces.evals.external.create(
            workspace_id="workspace_id",
            eval_id="eval_id",
            eval_type="external",
            omni_model_id="omni_model_id",
        )
        assert_matches_type(object, external, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.workspaces.evals.external.with_raw_response.create(
            workspace_id="workspace_id",
            eval_id="eval_id",
            eval_type="external",
            omni_model_id="omni_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = await response.parse()
        assert_matches_type(object, external, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOmnistack) -> None:
        async with async_client.workspaces.evals.external.with_streaming_response.create(
            workspace_id="workspace_id",
            eval_id="eval_id",
            eval_type="external",
            omni_model_id="omni_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = await response.parse()
            assert_matches_type(object, external, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.evals.external.with_raw_response.create(
                workspace_id="",
                eval_id="eval_id",
                eval_type="external",
                omni_model_id="omni_model_id",
            )
