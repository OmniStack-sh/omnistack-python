# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RequestCountryDistribution", "ChartData"]


class ChartData(BaseModel):
    city: str

    country: str

    requests: int


class RequestCountryDistribution(BaseModel):
    chart_data: List[ChartData]
