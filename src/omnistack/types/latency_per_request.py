# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["LatencyPerRequest", "ChartData", "ChartDataLatencyChart", "ChartDataOmnistackDeployedLatencyChart"]


class ChartDataLatencyChart(BaseModel):
    input_token_size: int

    latency: float

    output_token_size: int

    timestamp: datetime


class ChartDataOmnistackDeployedLatencyChart(BaseModel):
    inference_latency: float

    input_token_size: int

    output_token_size: int

    timestamp: datetime

    total_latency: float

    worker_startup_latency: float


ChartData: TypeAlias = Union[ChartDataLatencyChart, ChartDataOmnistackDeployedLatencyChart]


class LatencyPerRequest(BaseModel):
    avg_latency: float

    chart_data: List[ChartData]
