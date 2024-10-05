# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObservability:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_inference(self, client: Omnistack) -> None:
        observability = client.observability.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, observability, path=["response"])

    @parametrize
    def test_method_inference_with_all_params(self, client: Omnistack) -> None:
        observability = client.observability.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            page=1,
            page_size=1,
            request_type="request_type",
        )
        assert_matches_type(object, observability, path=["response"])

    @parametrize
    def test_raw_response_inference(self, client: Omnistack) -> None:
        response = client.observability.with_raw_response.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observability = response.parse()
        assert_matches_type(object, observability, path=["response"])

    @parametrize
    def test_streaming_response_inference(self, client: Omnistack) -> None:
        with client.observability.with_streaming_response.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observability = response.parse()
            assert_matches_type(object, observability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_inference(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.observability.with_raw_response.inference(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.observability.with_raw_response.inference(
                omni_model_id="",
                workspace_id="workspace_id",
            )


class TestAsyncObservability:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_inference(self, async_client: AsyncOmnistack) -> None:
        observability = await async_client.observability.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, observability, path=["response"])

    @parametrize
    async def test_method_inference_with_all_params(self, async_client: AsyncOmnistack) -> None:
        observability = await async_client.observability.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
            page=1,
            page_size=1,
            request_type="request_type",
        )
        assert_matches_type(object, observability, path=["response"])

    @parametrize
    async def test_raw_response_inference(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.observability.with_raw_response.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        observability = await response.parse()
        assert_matches_type(object, observability, path=["response"])

    @parametrize
    async def test_streaming_response_inference(self, async_client: AsyncOmnistack) -> None:
        async with async_client.observability.with_streaming_response.inference(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            observability = await response.parse()
            assert_matches_type(object, observability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_inference(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.observability.with_raw_response.inference(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.observability.with_raw_response.inference(
                omni_model_id="",
                workspace_id="workspace_id",
            )
