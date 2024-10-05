# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectFetchExternalProviderParams"]


class ConnectFetchExternalProviderParams(TypedDict, total=False):
    model_provider: Required[Literal["openai", "groq", "claudi"]]

    provider_api_key: Required[str]
