# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_completions(self, client: Omnistack) -> None:
        chat = client.openai.chat.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-4o",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_method_completions_with_all_params(self, client: Omnistack) -> None:
        chat = client.openai.chat.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "name": "name",
                }
            ],
            model="gpt-4o",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=1,
            omni_params={"foo": "string"},
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "text"},
            seed=-9007199254740991,
            service_tier="auto",
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                },
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                },
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                },
            ],
            top_logprobs=0,
            top_p=1,
            user="user-1234",
            workspace_id_temp="workspace-id-temp",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_completions(self, client: Omnistack) -> None:
        response = client.openai.chat.with_raw_response.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-4o",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_completions(self, client: Omnistack) -> None:
        with client.openai.chat.with_streaming_response.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-4o",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_completions(self, async_client: AsyncOmnistack) -> None:
        chat = await async_client.openai.chat.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-4o",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_method_completions_with_all_params(self, async_client: AsyncOmnistack) -> None:
        chat = await async_client.openai.chat.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "name": "name",
                }
            ],
            model="gpt-4o",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=1,
            omni_params={"foo": "string"},
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "text"},
            seed=-9007199254740991,
            service_tier="auto",
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                },
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                },
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                        "strict": True,
                    },
                    "type": "function",
                },
            ],
            top_logprobs=0,
            top_p=1,
            user="user-1234",
            workspace_id_temp="workspace-id-temp",
        )
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_completions(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.openai.chat.with_raw_response.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-4o",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_completions(self, async_client: AsyncOmnistack) -> None:
        async with async_client.openai.chat.with_streaming_response.completions(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-4o",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
