# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types.workspaces.api_keys import (
    SimpleListResponse,
    SimpleCreateResponse,
    SimpleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimple:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Omnistack) -> None:
        simple = client.workspaces.api_keys.simple.create(
            workspace_id="workspace_id",
            access_type="MODEL",
            api_key_name="api_key_name",
        )
        assert_matches_type(SimpleCreateResponse, simple, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Omnistack) -> None:
        response = client.workspaces.api_keys.simple.with_raw_response.create(
            workspace_id="workspace_id",
            access_type="MODEL",
            api_key_name="api_key_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleCreateResponse, simple, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Omnistack) -> None:
        with client.workspaces.api_keys.simple.with_streaming_response.create(
            workspace_id="workspace_id",
            access_type="MODEL",
            api_key_name="api_key_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleCreateResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.api_keys.simple.with_raw_response.create(
                workspace_id="",
                access_type="MODEL",
                api_key_name="api_key_name",
            )

    @parametrize
    def test_method_list(self, client: Omnistack) -> None:
        simple = client.workspaces.api_keys.simple.list(
            "workspace_id",
        )
        assert_matches_type(SimpleListResponse, simple, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Omnistack) -> None:
        response = client.workspaces.api_keys.simple.with_raw_response.list(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleListResponse, simple, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Omnistack) -> None:
        with client.workspaces.api_keys.simple.with_streaming_response.list(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleListResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.api_keys.simple.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Omnistack) -> None:
        simple = client.workspaces.api_keys.simple.delete(
            api_key_id="api_key_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SimpleDeleteResponse, simple, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Omnistack) -> None:
        response = client.workspaces.api_keys.simple.with_raw_response.delete(
            api_key_id="api_key_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = response.parse()
        assert_matches_type(SimpleDeleteResponse, simple, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Omnistack) -> None:
        with client.workspaces.api_keys.simple.with_streaming_response.delete(
            api_key_id="api_key_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = response.parse()
            assert_matches_type(SimpleDeleteResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.api_keys.simple.with_raw_response.delete(
                api_key_id="api_key_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            client.workspaces.api_keys.simple.with_raw_response.delete(
                api_key_id="",
                workspace_id="workspace_id",
            )


class TestAsyncSimple:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOmnistack) -> None:
        simple = await async_client.workspaces.api_keys.simple.create(
            workspace_id="workspace_id",
            access_type="MODEL",
            api_key_name="api_key_name",
        )
        assert_matches_type(SimpleCreateResponse, simple, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.workspaces.api_keys.simple.with_raw_response.create(
            workspace_id="workspace_id",
            access_type="MODEL",
            api_key_name="api_key_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleCreateResponse, simple, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOmnistack) -> None:
        async with async_client.workspaces.api_keys.simple.with_streaming_response.create(
            workspace_id="workspace_id",
            access_type="MODEL",
            api_key_name="api_key_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleCreateResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.api_keys.simple.with_raw_response.create(
                workspace_id="",
                access_type="MODEL",
                api_key_name="api_key_name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOmnistack) -> None:
        simple = await async_client.workspaces.api_keys.simple.list(
            "workspace_id",
        )
        assert_matches_type(SimpleListResponse, simple, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.workspaces.api_keys.simple.with_raw_response.list(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleListResponse, simple, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOmnistack) -> None:
        async with async_client.workspaces.api_keys.simple.with_streaming_response.list(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleListResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.api_keys.simple.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOmnistack) -> None:
        simple = await async_client.workspaces.api_keys.simple.delete(
            api_key_id="api_key_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SimpleDeleteResponse, simple, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.workspaces.api_keys.simple.with_raw_response.delete(
            api_key_id="api_key_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple = await response.parse()
        assert_matches_type(SimpleDeleteResponse, simple, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOmnistack) -> None:
        async with async_client.workspaces.api_keys.simple.with_streaming_response.delete(
            api_key_id="api_key_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple = await response.parse()
            assert_matches_type(SimpleDeleteResponse, simple, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.api_keys.simple.with_raw_response.delete(
                api_key_id="api_key_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
            await async_client.workspaces.api_keys.simple.with_raw_response.delete(
                api_key_id="",
                workspace_id="workspace_id",
            )
