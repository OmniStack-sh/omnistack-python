# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import OmniProxyCreateResponse, OmniProxyDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOmniProxies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Omnistack) -> None:
        omni_proxy = client.omni_proxies.create(
            workspace_id="workspace_id",
            omni_model_id="omni_model_id",
            omniproxy_id="omniproxy_id",
        )
        assert_matches_type(OmniProxyCreateResponse, omni_proxy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Omnistack) -> None:
        response = client.omni_proxies.with_raw_response.create(
            workspace_id="workspace_id",
            omni_model_id="omni_model_id",
            omniproxy_id="omniproxy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_proxy = response.parse()
        assert_matches_type(OmniProxyCreateResponse, omni_proxy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Omnistack) -> None:
        with client.omni_proxies.with_streaming_response.create(
            workspace_id="workspace_id",
            omni_model_id="omni_model_id",
            omniproxy_id="omniproxy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_proxy = response.parse()
            assert_matches_type(OmniProxyCreateResponse, omni_proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.omni_proxies.with_raw_response.create(
                workspace_id="",
                omni_model_id="omni_model_id",
                omniproxy_id="omniproxy_id",
            )

    @parametrize
    def test_method_delete(self, client: Omnistack) -> None:
        omni_proxy = client.omni_proxies.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(OmniProxyDeleteResponse, omni_proxy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Omnistack) -> None:
        response = client.omni_proxies.with_raw_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_proxy = response.parse()
        assert_matches_type(OmniProxyDeleteResponse, omni_proxy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Omnistack) -> None:
        with client.omni_proxies.with_streaming_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_proxy = response.parse()
            assert_matches_type(OmniProxyDeleteResponse, omni_proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.omni_proxies.with_raw_response.delete(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            client.omni_proxies.with_raw_response.delete(
                omni_model_id="",
                workspace_id="workspace_id",
            )


class TestAsyncOmniProxies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOmnistack) -> None:
        omni_proxy = await async_client.omni_proxies.create(
            workspace_id="workspace_id",
            omni_model_id="omni_model_id",
            omniproxy_id="omniproxy_id",
        )
        assert_matches_type(OmniProxyCreateResponse, omni_proxy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.omni_proxies.with_raw_response.create(
            workspace_id="workspace_id",
            omni_model_id="omni_model_id",
            omniproxy_id="omniproxy_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_proxy = await response.parse()
        assert_matches_type(OmniProxyCreateResponse, omni_proxy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOmnistack) -> None:
        async with async_client.omni_proxies.with_streaming_response.create(
            workspace_id="workspace_id",
            omni_model_id="omni_model_id",
            omniproxy_id="omniproxy_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_proxy = await response.parse()
            assert_matches_type(OmniProxyCreateResponse, omni_proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.omni_proxies.with_raw_response.create(
                workspace_id="",
                omni_model_id="omni_model_id",
                omniproxy_id="omniproxy_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOmnistack) -> None:
        omni_proxy = await async_client.omni_proxies.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(OmniProxyDeleteResponse, omni_proxy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.omni_proxies.with_raw_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        omni_proxy = await response.parse()
        assert_matches_type(OmniProxyDeleteResponse, omni_proxy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOmnistack) -> None:
        async with async_client.omni_proxies.with_streaming_response.delete(
            omni_model_id="omni_model_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            omni_proxy = await response.parse()
            assert_matches_type(OmniProxyDeleteResponse, omni_proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.omni_proxies.with_raw_response.delete(
                omni_model_id="omni_model_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `omni_model_id` but received ''"):
            await async_client.omni_proxies.with_raw_response.delete(
                omni_model_id="",
                workspace_id="workspace_id",
            )
