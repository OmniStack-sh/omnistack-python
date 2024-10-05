# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import (
    CustomModelListResponse,
    CustomModelDeleteResponse,
    CustomModelDeployResponse,
    CustomModelRetrieveResponse,
    CustomModelFetchCustomModelResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Omnistack) -> None:
        custom_model = client.custom_models.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(CustomModelRetrieveResponse, custom_model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Omnistack) -> None:
        response = client.custom_models.with_raw_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = response.parse()
        assert_matches_type(CustomModelRetrieveResponse, custom_model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Omnistack) -> None:
        with client.custom_models.with_streaming_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = response.parse()
            assert_matches_type(CustomModelRetrieveResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.custom_models.with_raw_response.retrieve(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.custom_models.with_raw_response.retrieve(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Omnistack) -> None:
        custom_model = client.custom_models.list(
            "workspace_id",
        )
        assert_matches_type(CustomModelListResponse, custom_model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Omnistack) -> None:
        response = client.custom_models.with_raw_response.list(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = response.parse()
        assert_matches_type(CustomModelListResponse, custom_model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Omnistack) -> None:
        with client.custom_models.with_streaming_response.list(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = response.parse()
            assert_matches_type(CustomModelListResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.custom_models.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Omnistack) -> None:
        custom_model = client.custom_models.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(CustomModelDeleteResponse, custom_model, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Omnistack) -> None:
        response = client.custom_models.with_raw_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = response.parse()
        assert_matches_type(CustomModelDeleteResponse, custom_model, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Omnistack) -> None:
        with client.custom_models.with_streaming_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = response.parse()
            assert_matches_type(CustomModelDeleteResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.custom_models.with_raw_response.delete(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.custom_models.with_raw_response.delete(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_deploy(self, client: Omnistack) -> None:
        custom_model = client.custom_models.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
        )
        assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

    @parametrize
    def test_method_deploy_with_all_params(self, client: Omnistack) -> None:
        custom_model = client.custom_models.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
            active_gpu_worker=0,
            execution_timeout=0,
            gpu_idle_timeout=0,
            max_gpu_worker=0,
            scale_type="QUEUE_DELAY",
            scaler_value=0,
        )
        assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

    @parametrize
    def test_raw_response_deploy(self, client: Omnistack) -> None:
        response = client.custom_models.with_raw_response.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = response.parse()
        assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

    @parametrize
    def test_streaming_response_deploy(self, client: Omnistack) -> None:
        with client.custom_models.with_streaming_response.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = response.parse()
            assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deploy(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.custom_models.with_raw_response.deploy(
                workspace_id="",
                gpu_type="gpu_type",
                hf_id="hf_id",
                hf_token="hf_token",
                omni_model_id="omni_model_id",
            )

    @parametrize
    def test_method_fetch_custom_model(self, client: Omnistack) -> None:
        custom_model = client.custom_models.fetch_custom_model(
            workspace_id="workspace_id",
            hf_id="hf_id",
            hf_token="hf_token",
        )
        assert_matches_type(CustomModelFetchCustomModelResponse, custom_model, path=["response"])

    @parametrize
    def test_raw_response_fetch_custom_model(self, client: Omnistack) -> None:
        response = client.custom_models.with_raw_response.fetch_custom_model(
            workspace_id="workspace_id",
            hf_id="hf_id",
            hf_token="hf_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = response.parse()
        assert_matches_type(CustomModelFetchCustomModelResponse, custom_model, path=["response"])

    @parametrize
    def test_streaming_response_fetch_custom_model(self, client: Omnistack) -> None:
        with client.custom_models.with_streaming_response.fetch_custom_model(
            workspace_id="workspace_id",
            hf_id="hf_id",
            hf_token="hf_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = response.parse()
            assert_matches_type(CustomModelFetchCustomModelResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_custom_model(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.custom_models.with_raw_response.fetch_custom_model(
                workspace_id="",
                hf_id="hf_id",
                hf_token="hf_token",
            )


class TestAsyncCustomModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOmnistack) -> None:
        custom_model = await async_client.custom_models.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(CustomModelRetrieveResponse, custom_model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.custom_models.with_raw_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = await response.parse()
        assert_matches_type(CustomModelRetrieveResponse, custom_model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        async with async_client.custom_models.with_streaming_response.retrieve(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = await response.parse()
            assert_matches_type(CustomModelRetrieveResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.custom_models.with_raw_response.retrieve(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.custom_models.with_raw_response.retrieve(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOmnistack) -> None:
        custom_model = await async_client.custom_models.list(
            "workspace_id",
        )
        assert_matches_type(CustomModelListResponse, custom_model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.custom_models.with_raw_response.list(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = await response.parse()
        assert_matches_type(CustomModelListResponse, custom_model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOmnistack) -> None:
        async with async_client.custom_models.with_streaming_response.list(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = await response.parse()
            assert_matches_type(CustomModelListResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.custom_models.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOmnistack) -> None:
        custom_model = await async_client.custom_models.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(CustomModelDeleteResponse, custom_model, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.custom_models.with_raw_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = await response.parse()
        assert_matches_type(CustomModelDeleteResponse, custom_model, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOmnistack) -> None:
        async with async_client.custom_models.with_streaming_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = await response.parse()
            assert_matches_type(CustomModelDeleteResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.custom_models.with_raw_response.delete(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.custom_models.with_raw_response.delete(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_deploy(self, async_client: AsyncOmnistack) -> None:
        custom_model = await async_client.custom_models.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
        )
        assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

    @parametrize
    async def test_method_deploy_with_all_params(self, async_client: AsyncOmnistack) -> None:
        custom_model = await async_client.custom_models.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
            active_gpu_worker=0,
            execution_timeout=0,
            gpu_idle_timeout=0,
            max_gpu_worker=0,
            scale_type="QUEUE_DELAY",
            scaler_value=0,
        )
        assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

    @parametrize
    async def test_raw_response_deploy(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.custom_models.with_raw_response.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = await response.parse()
        assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

    @parametrize
    async def test_streaming_response_deploy(self, async_client: AsyncOmnistack) -> None:
        async with async_client.custom_models.with_streaming_response.deploy(
            workspace_id="workspace_id",
            gpu_type="gpu_type",
            hf_id="hf_id",
            hf_token="hf_token",
            omni_model_id="omni_model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = await response.parse()
            assert_matches_type(CustomModelDeployResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deploy(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.custom_models.with_raw_response.deploy(
                workspace_id="",
                gpu_type="gpu_type",
                hf_id="hf_id",
                hf_token="hf_token",
                omni_model_id="omni_model_id",
            )

    @parametrize
    async def test_method_fetch_custom_model(self, async_client: AsyncOmnistack) -> None:
        custom_model = await async_client.custom_models.fetch_custom_model(
            workspace_id="workspace_id",
            hf_id="hf_id",
            hf_token="hf_token",
        )
        assert_matches_type(CustomModelFetchCustomModelResponse, custom_model, path=["response"])

    @parametrize
    async def test_raw_response_fetch_custom_model(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.custom_models.with_raw_response.fetch_custom_model(
            workspace_id="workspace_id",
            hf_id="hf_id",
            hf_token="hf_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_model = await response.parse()
        assert_matches_type(CustomModelFetchCustomModelResponse, custom_model, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_custom_model(self, async_client: AsyncOmnistack) -> None:
        async with async_client.custom_models.with_streaming_response.fetch_custom_model(
            workspace_id="workspace_id",
            hf_id="hf_id",
            hf_token="hf_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_model = await response.parse()
            assert_matches_type(CustomModelFetchCustomModelResponse, custom_model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_custom_model(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.custom_models.with_raw_response.fetch_custom_model(
                workspace_id="",
                hf_id="hf_id",
                hf_token="hf_token",
            )
