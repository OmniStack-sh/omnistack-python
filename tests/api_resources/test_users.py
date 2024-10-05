# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import UserLoginResponse, UserRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Omnistack) -> None:
        user = client.users.retrieve()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Omnistack) -> None:
        response = client.users.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Omnistack) -> None:
        with client.users.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_login(self, client: Omnistack) -> None:
        user = client.users.login()
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    def test_method_login_with_all_params(self, client: Omnistack) -> None:
        user = client.users.login(
            about_user="xxxxxxxxxx",
            how_did_you_hear_about_us="xxxxx",
        )
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    def test_raw_response_login(self, client: Omnistack) -> None:
        response = client.users.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_login(self, client: Omnistack) -> None:
        with client.users.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserLoginResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOmnistack) -> None:
        user = await async_client.users.retrieve()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.users.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        async with async_client.users.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_login(self, async_client: AsyncOmnistack) -> None:
        user = await async_client.users.login()
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncOmnistack) -> None:
        user = await async_client.users.login(
            about_user="xxxxxxxxxx",
            how_did_you_hear_about_us="xxxxx",
        )
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_login(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.users.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncOmnistack) -> None:
        async with async_client.users.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserLoginResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
