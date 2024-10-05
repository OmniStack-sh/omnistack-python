# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import (
    ConnectListResponse,
    ConnectDeleteResponse,
    ConnectDeployResponse,
    ConnectFetchExternalProviderResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Omnistack) -> None:
        connect = client.connect.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(ConnectListResponse, connect, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Omnistack) -> None:
        connect = client.connect.list(
            workspace_id="workspace_id",
            provider_id="provider_id",
        )
        assert_matches_type(ConnectListResponse, connect, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Omnistack) -> None:
        response = client.connect.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectListResponse, connect, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Omnistack) -> None:
        with client.connect.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectListResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.connect.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Omnistack) -> None:
        connect = client.connect.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(ConnectDeleteResponse, connect, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Omnistack) -> None:
        response = client.connect.with_raw_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectDeleteResponse, connect, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Omnistack) -> None:
        with client.connect.with_streaming_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectDeleteResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.connect.with_raw_response.delete(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.connect.with_raw_response.delete(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_deploy(self, client: Omnistack) -> None:
        connect = client.connect.deploy(
            workspace_id="workspace_id",
            model_provider="openai",
            omni_model_id="omni_model_id",
            provide_model_id="provide_model_id",
            provider_api_key="provider_api_key",
        )
        assert_matches_type(ConnectDeployResponse, connect, path=["response"])

    @parametrize
    def test_raw_response_deploy(self, client: Omnistack) -> None:
        response = client.connect.with_raw_response.deploy(
            workspace_id="workspace_id",
            model_provider="openai",
            omni_model_id="omni_model_id",
            provide_model_id="provide_model_id",
            provider_api_key="provider_api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectDeployResponse, connect, path=["response"])

    @parametrize
    def test_streaming_response_deploy(self, client: Omnistack) -> None:
        with client.connect.with_streaming_response.deploy(
            workspace_id="workspace_id",
            model_provider="openai",
            omni_model_id="omni_model_id",
            provide_model_id="provide_model_id",
            provider_api_key="provider_api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectDeployResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deploy(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.connect.with_raw_response.deploy(
                workspace_id="",
                model_provider="openai",
                omni_model_id="omni_model_id",
                provide_model_id="provide_model_id",
                provider_api_key="provider_api_key",
            )

    @parametrize
    def test_method_fetch_external_provider(self, client: Omnistack) -> None:
        connect = client.connect.fetch_external_provider(
            workspace_id="workspace_id",
            model_provider="openai",
            provider_api_key="provider_api_key",
        )
        assert_matches_type(ConnectFetchExternalProviderResponse, connect, path=["response"])

    @parametrize
    def test_raw_response_fetch_external_provider(self, client: Omnistack) -> None:
        response = client.connect.with_raw_response.fetch_external_provider(
            workspace_id="workspace_id",
            model_provider="openai",
            provider_api_key="provider_api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectFetchExternalProviderResponse, connect, path=["response"])

    @parametrize
    def test_streaming_response_fetch_external_provider(self, client: Omnistack) -> None:
        with client.connect.with_streaming_response.fetch_external_provider(
            workspace_id="workspace_id",
            model_provider="openai",
            provider_api_key="provider_api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectFetchExternalProviderResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_external_provider(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.connect.with_raw_response.fetch_external_provider(
                workspace_id="",
                model_provider="openai",
                provider_api_key="provider_api_key",
            )


class TestAsyncConnect:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOmnistack) -> None:
        connect = await async_client.connect.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(ConnectListResponse, connect, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOmnistack) -> None:
        connect = await async_client.connect.list(
            workspace_id="workspace_id",
            provider_id="provider_id",
        )
        assert_matches_type(ConnectListResponse, connect, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.connect.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectListResponse, connect, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOmnistack) -> None:
        async with async_client.connect.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectListResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.connect.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOmnistack) -> None:
        connect = await async_client.connect.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(ConnectDeleteResponse, connect, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.connect.with_raw_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectDeleteResponse, connect, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOmnistack) -> None:
        async with async_client.connect.with_streaming_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectDeleteResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.connect.with_raw_response.delete(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.connect.with_raw_response.delete(
                omni_model_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_deploy(self, async_client: AsyncOmnistack) -> None:
        connect = await async_client.connect.deploy(
            workspace_id="workspace_id",
            model_provider="openai",
            omni_model_id="omni_model_id",
            provide_model_id="provide_model_id",
            provider_api_key="provider_api_key",
        )
        assert_matches_type(ConnectDeployResponse, connect, path=["response"])

    @parametrize
    async def test_raw_response_deploy(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.connect.with_raw_response.deploy(
            workspace_id="workspace_id",
            model_provider="openai",
            omni_model_id="omni_model_id",
            provide_model_id="provide_model_id",
            provider_api_key="provider_api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectDeployResponse, connect, path=["response"])

    @parametrize
    async def test_streaming_response_deploy(self, async_client: AsyncOmnistack) -> None:
        async with async_client.connect.with_streaming_response.deploy(
            workspace_id="workspace_id",
            model_provider="openai",
            omni_model_id="omni_model_id",
            provide_model_id="provide_model_id",
            provider_api_key="provider_api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectDeployResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deploy(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.connect.with_raw_response.deploy(
                workspace_id="",
                model_provider="openai",
                omni_model_id="omni_model_id",
                provide_model_id="provide_model_id",
                provider_api_key="provider_api_key",
            )

    @parametrize
    async def test_method_fetch_external_provider(self, async_client: AsyncOmnistack) -> None:
        connect = await async_client.connect.fetch_external_provider(
            workspace_id="workspace_id",
            model_provider="openai",
            provider_api_key="provider_api_key",
        )
        assert_matches_type(ConnectFetchExternalProviderResponse, connect, path=["response"])

    @parametrize
    async def test_raw_response_fetch_external_provider(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.connect.with_raw_response.fetch_external_provider(
            workspace_id="workspace_id",
            model_provider="openai",
            provider_api_key="provider_api_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectFetchExternalProviderResponse, connect, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_external_provider(self, async_client: AsyncOmnistack) -> None:
        async with async_client.connect.with_streaming_response.fetch_external_provider(
            workspace_id="workspace_id",
            model_provider="openai",
            provider_api_key="provider_api_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectFetchExternalProviderResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_external_provider(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.connect.with_raw_response.fetch_external_provider(
                workspace_id="",
                model_provider="openai",
                provider_api_key="provider_api_key",
            )
