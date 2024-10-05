# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectDeployParams"]


class ConnectDeployParams(TypedDict, total=False):
    model_provider: Required[Literal["openai", "groq"]]

    omni_model_id: Required[str]

    provide_model_id: Required[str]

    provider_api_key: Required[str]
