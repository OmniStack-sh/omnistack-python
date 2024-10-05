# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomModelFetchCustomModelParams"]


class CustomModelFetchCustomModelParams(TypedDict, total=False):
    hf_id: Required[str]

    hf_token: Required[str]
