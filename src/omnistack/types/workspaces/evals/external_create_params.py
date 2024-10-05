# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalCreateParams"]


class ExternalCreateParams(TypedDict, total=False):
    eval_id: Required[str]

    eval_type: Required[Literal["external"]]

    omni_model_id: Required[str]
