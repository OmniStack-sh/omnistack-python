# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PromptSwitchVersionParams"]


class PromptSwitchVersionParams(TypedDict, total=False):
    workspace_id: Required[str]

    project_id: Required[str]

    version_number: Required[str]
