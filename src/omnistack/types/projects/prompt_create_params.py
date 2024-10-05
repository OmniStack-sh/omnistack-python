# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    workspace_id: Required[str]

    description: Required[str]

    name: Required[str]

    type: Required[List[Literal["chat", "completion"]]]
