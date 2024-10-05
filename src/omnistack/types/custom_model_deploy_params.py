# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomModelDeployParams"]


class CustomModelDeployParams(TypedDict, total=False):
    gpu_type: Required[str]

    hf_id: Required[str]

    hf_token: Required[str]

    omni_model_id: Required[str]

    active_gpu_worker: int

    execution_timeout: int

    gpu_idle_timeout: int

    max_gpu_worker: int

    scale_type: Literal["QUEUE_DELAY", "REQUEST_COUNT"]

    scaler_value: int
