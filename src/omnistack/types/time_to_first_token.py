# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["TimeToFirstToken", "ChartData"]


class ChartData(BaseModel):
    time_to_first_token: float

    timestamp: datetime


class TimeToFirstToken(BaseModel):
    avg_time: float

    chart_data: List[ChartData]
