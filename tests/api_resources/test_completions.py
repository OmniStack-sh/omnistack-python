# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Omnistack) -> None:
        completion = client.completions.create(
            model="string",
            prompt="This is a test.",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Omnistack) -> None:
        completion = client.completions.create(
            model="string",
            prompt="This is a test.",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=-9007199254740991,
            stop="\n",
            stream=True,
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Omnistack) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Omnistack) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOmnistack) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOmnistack) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=-9007199254740991,
            stop="\n",
            stream=True,
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOmnistack) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
