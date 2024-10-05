# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .cost_per_request import CostPerRequest

__all__ = [
    "ModelsDashboardOverviewCostPerRequestResponse",
    "OmnistackDeployedCostPerRequest",
    "OmnistackDeployedCostPerRequestChartData",
    "OmnistackDeployedCostPerRequestChartDataCost",
    "OmnistackDeployedCostPerRequestTotalCost",
]


class OmnistackDeployedCostPerRequestChartDataCost(BaseModel):
    cost: float

    currency: str


class OmnistackDeployedCostPerRequestChartData(BaseModel):
    cost: OmnistackDeployedCostPerRequestChartDataCost

    timestamp: datetime


class OmnistackDeployedCostPerRequestTotalCost(BaseModel):
    cost: float

    currency: str


class OmnistackDeployedCostPerRequest(BaseModel):
    chart_data: List[OmnistackDeployedCostPerRequestChartData]

    total_cost: OmnistackDeployedCostPerRequestTotalCost


ModelsDashboardOverviewCostPerRequestResponse: TypeAlias = Union[CostPerRequest, OmnistackDeployedCostPerRequest]
