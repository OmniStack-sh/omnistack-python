# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "CostPerRequest",
    "ChartData",
    "ChartDataInputCost",
    "ChartDataOutputCost",
    "TotalCost",
    "TotalInputCost",
    "TotalOutputCost",
]


class ChartDataInputCost(BaseModel):
    cost: float

    currency: str


class ChartDataOutputCost(BaseModel):
    cost: float

    currency: str


class ChartData(BaseModel):
    input_cost: ChartDataInputCost

    output_cost: ChartDataOutputCost

    timestamp: datetime


class TotalCost(BaseModel):
    cost: float

    currency: str


class TotalInputCost(BaseModel):
    cost: float

    currency: str


class TotalOutputCost(BaseModel):
    cost: float

    currency: str


class CostPerRequest(BaseModel):
    chart_data: List[ChartData]

    total_cost: TotalCost

    total_input_cost: TotalInputCost

    total_output_cost: TotalOutputCost
