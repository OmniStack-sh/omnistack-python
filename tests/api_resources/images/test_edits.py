# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import ImageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEdits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Omnistack) -> None:
        edit = client.images.edits.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )
        assert_matches_type(ImageResponse, edit, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Omnistack) -> None:
        edit = client.images.edits.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
            mask=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="256x256",
            user="user-1234",
        )
        assert_matches_type(ImageResponse, edit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Omnistack) -> None:
        response = client.images.edits.with_raw_response.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit = response.parse()
        assert_matches_type(ImageResponse, edit, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Omnistack) -> None:
        with client.images.edits.with_streaming_response.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit = response.parse()
            assert_matches_type(ImageResponse, edit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEdits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOmnistack) -> None:
        edit = await async_client.images.edits.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )
        assert_matches_type(ImageResponse, edit, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOmnistack) -> None:
        edit = await async_client.images.edits.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
            mask=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="256x256",
            user="user-1234",
        )
        assert_matches_type(ImageResponse, edit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.images.edits.with_raw_response.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit = await response.parse()
        assert_matches_type(ImageResponse, edit, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOmnistack) -> None:
        async with async_client.images.edits.with_streaming_response.create(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit = await response.parse()
            assert_matches_type(ImageResponse, edit, path=["response"])

        assert cast(Any, response.is_closed) is True
