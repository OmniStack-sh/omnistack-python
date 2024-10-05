# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CustomModelRetrieveResponse", "Status", "Overview"]


class Status(BaseModel):
    deployment: str

    message: str

    progress: float


class Overview(BaseModel):
    cost: float

    deployment: str

    expected_total_time: float

    expected_tps: float

    expected_ttft: float

    omni_model_id: str

    test_case: str


class CustomModelRetrieveResponse(BaseModel):
    status: Status

    overview: Optional[Overview] = None
