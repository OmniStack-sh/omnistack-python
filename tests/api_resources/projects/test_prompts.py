# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from omnistack import Omnistack, AsyncOmnistack
from tests.utils import assert_matches_type
from omnistack.types.projects import (
    GetPromptResponse,
    PromptListResponse,
    CreatePromptResponse,
    PromptDeleteResponse,
    PromptUpdateResponse,
    PromptSwitchVersionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.create(
            project_id="project_id",
            workspace_id="workspace_id",
            description="description",
            name="name",
            type=["chat", "completion"],
        )
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Omnistack) -> None:
        response = client.projects.prompts.with_raw_response.create(
            project_id="project_id",
            workspace_id="workspace_id",
            description="description",
            name="name",
            type=["chat", "completion"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Omnistack) -> None:
        with client.projects.prompts.with_streaming_response.create(
            project_id="project_id",
            workspace_id="workspace_id",
            description="description",
            name="name",
            type=["chat", "completion"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(CreatePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.projects.prompts.with_raw_response.create(
                project_id="project_id",
                workspace_id="",
                description="description",
                name="name",
                type=["chat", "completion"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.prompts.with_raw_response.create(
                project_id="",
                workspace_id="workspace_id",
                description="description",
                name="name",
                type=["chat", "completion"],
            )

    @parametrize
    def test_method_retrieve(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        )
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Omnistack) -> None:
        response = client.projects.prompts.with_raw_response.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Omnistack) -> None:
        with client.projects.prompts.with_streaming_response.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(GetPromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.projects.prompts.with_raw_response.retrieve(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.prompts.with_raw_response.retrieve(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.projects.prompts.with_raw_response.retrieve(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
            )

    @parametrize
    def test_method_update(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.update(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            commit_message="commit_message",
            settings={"foo": {}},
            type=["chat", "completion"],
        )
        assert_matches_type(PromptUpdateResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Omnistack) -> None:
        response = client.projects.prompts.with_raw_response.update(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            commit_message="commit_message",
            settings={"foo": {}},
            type=["chat", "completion"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptUpdateResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Omnistack) -> None:
        with client.projects.prompts.with_streaming_response.update(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            commit_message="commit_message",
            settings={"foo": {}},
            type=["chat", "completion"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptUpdateResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.projects.prompts.with_raw_response.update(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
                commit_message="commit_message",
                settings={"foo": {}},
                type=["chat", "completion"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.prompts.with_raw_response.update(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
                commit_message="commit_message",
                settings={"foo": {}},
                type=["chat", "completion"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.projects.prompts.with_raw_response.update(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
                commit_message="commit_message",
                settings={"foo": {}},
                type=["chat", "completion"],
            )

    @parametrize
    def test_method_list(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.list(
            project_id="project_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Omnistack) -> None:
        response = client.projects.prompts.with_raw_response.list(
            project_id="project_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Omnistack) -> None:
        with client.projects.prompts.with_streaming_response.list(
            project_id="project_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.projects.prompts.with_raw_response.list(
                project_id="project_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.prompts.with_raw_response.list(
                project_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_delete(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.delete(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Omnistack) -> None:
        response = client.projects.prompts.with_raw_response.delete(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Omnistack) -> None:
        with client.projects.prompts.with_streaming_response.delete(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.projects.prompts.with_raw_response.delete(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.prompts.with_raw_response.delete(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.projects.prompts.with_raw_response.delete(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
            )

    @parametrize
    def test_method_switch_version(self, client: Omnistack) -> None:
        prompt = client.projects.prompts.switch_version(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        )
        assert_matches_type(PromptSwitchVersionResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_switch_version(self, client: Omnistack) -> None:
        response = client.projects.prompts.with_raw_response.switch_version(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptSwitchVersionResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_switch_version(self, client: Omnistack) -> None:
        with client.projects.prompts.with_streaming_response.switch_version(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptSwitchVersionResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_switch_version(self, client: Omnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.projects.prompts.with_raw_response.switch_version(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
                version_number="version_number",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.prompts.with_raw_response.switch_version(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
                version_number="version_number",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.projects.prompts.with_raw_response.switch_version(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
                version_number="version_number",
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.create(
            project_id="project_id",
            workspace_id="workspace_id",
            description="description",
            name="name",
            type=["chat", "completion"],
        )
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.projects.prompts.with_raw_response.create(
            project_id="project_id",
            workspace_id="workspace_id",
            description="description",
            name="name",
            type=["chat", "completion"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOmnistack) -> None:
        async with async_client.projects.prompts.with_streaming_response.create(
            project_id="project_id",
            workspace_id="workspace_id",
            description="description",
            name="name",
            type=["chat", "completion"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(CreatePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.create(
                project_id="project_id",
                workspace_id="",
                description="description",
                name="name",
                type=["chat", "completion"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.create(
                project_id="",
                workspace_id="workspace_id",
                description="description",
                name="name",
                type=["chat", "completion"],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        )
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.projects.prompts.with_raw_response.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOmnistack) -> None:
        async with async_client.projects.prompts.with_streaming_response.retrieve(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(GetPromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.retrieve(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.retrieve(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.retrieve(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.update(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            commit_message="commit_message",
            settings={"foo": {}},
            type=["chat", "completion"],
        )
        assert_matches_type(PromptUpdateResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.projects.prompts.with_raw_response.update(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            commit_message="commit_message",
            settings={"foo": {}},
            type=["chat", "completion"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptUpdateResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOmnistack) -> None:
        async with async_client.projects.prompts.with_streaming_response.update(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            commit_message="commit_message",
            settings={"foo": {}},
            type=["chat", "completion"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptUpdateResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.update(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
                commit_message="commit_message",
                settings={"foo": {}},
                type=["chat", "completion"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.update(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
                commit_message="commit_message",
                settings={"foo": {}},
                type=["chat", "completion"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.update(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
                commit_message="commit_message",
                settings={"foo": {}},
                type=["chat", "completion"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.list(
            project_id="project_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.projects.prompts.with_raw_response.list(
            project_id="project_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOmnistack) -> None:
        async with async_client.projects.prompts.with_streaming_response.list(
            project_id="project_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.list(
                project_id="project_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.list(
                project_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.delete(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.projects.prompts.with_raw_response.delete(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOmnistack) -> None:
        async with async_client.projects.prompts.with_streaming_response.delete(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.delete(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.delete(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.delete(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
            )

    @parametrize
    async def test_method_switch_version(self, async_client: AsyncOmnistack) -> None:
        prompt = await async_client.projects.prompts.switch_version(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        )
        assert_matches_type(PromptSwitchVersionResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_switch_version(self, async_client: AsyncOmnistack) -> None:
        response = await async_client.projects.prompts.with_raw_response.switch_version(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptSwitchVersionResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_switch_version(self, async_client: AsyncOmnistack) -> None:
        async with async_client.projects.prompts.with_streaming_response.switch_version(
            prompt_id="prompt_id",
            workspace_id="workspace_id",
            project_id="project_id",
            version_number="version_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptSwitchVersionResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_switch_version(self, async_client: AsyncOmnistack) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.switch_version(
                prompt_id="prompt_id",
                workspace_id="",
                project_id="project_id",
                version_number="version_number",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.switch_version(
                prompt_id="prompt_id",
                workspace_id="workspace_id",
                project_id="",
                version_number="version_number",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.projects.prompts.with_raw_response.switch_version(
                prompt_id="",
                workspace_id="workspace_id",
                project_id="project_id",
                version_number="version_number",
            )
