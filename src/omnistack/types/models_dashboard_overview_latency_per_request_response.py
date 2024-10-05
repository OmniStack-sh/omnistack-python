# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .latency_per_request import LatencyPerRequest

__all__ = [
    "ModelsDashboardOverviewLatencyPerRequestResponse",
    "OmnistackDeployedLatencyPerRequest",
    "OmnistackDeployedLatencyPerRequestChartData",
]


class OmnistackDeployedLatencyPerRequestChartData(BaseModel):
    inference_latency: float

    input_token_size: int

    output_token_size: int

    timestamp: datetime

    total_latency: float

    worker_startup_latency: float


class OmnistackDeployedLatencyPerRequest(BaseModel):
    avg_inference_latency: float

    avg_total_latency: float

    avg_worker_startup_latency: float

    chart_data: List[OmnistackDeployedLatencyPerRequestChartData]


ModelsDashboardOverviewLatencyPerRequestResponse: TypeAlias = Union[
    LatencyPerRequest, OmnistackDeployedLatencyPerRequest
]
