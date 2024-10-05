# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["RequestData", "ChartData"]


class ChartData(BaseModel):
    errors: int

    requests: int

    success: int

    timestamp: datetime


class RequestData(BaseModel):
    chart_data: List[ChartData]

    total_requests: int
