# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["TokensPerRequest", "ChartData"]


class ChartData(BaseModel):
    input_tokens: int

    output_tokens: int

    timestamp: datetime


class TokensPerRequest(BaseModel):
    chart_data: List[ChartData]

    total_input_tokens: float

    total_output_tokens: float

    total_tokens: float
