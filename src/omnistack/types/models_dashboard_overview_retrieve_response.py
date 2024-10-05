# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModelsDashboardOverviewRetrieveResponse",
    "ExternalModelConnectionsStatus",
    "ExternalModelConnectionsStatusStats",
    "OmnistackDeployedModels",
    "OmnistackDeployedModelsStats",
]


class ExternalModelConnectionsStatusStats(BaseModel):
    remaining_request_limit: int

    remaining_token_limit: int

    supported_inference: List[str]


class ExternalModelConnectionsStatus(BaseModel):
    available_stats: List[str]

    last_updated: datetime

    api_model_type: Literal["external_model_connections", "proxy_models"] = FieldInfo(alias="model_type")

    omni_model_id: str

    stats: Optional[ExternalModelConnectionsStatusStats] = None

    status: Literal["normal", "failed", "warning", "throttled"]


class OmnistackDeployedModelsStats(BaseModel):
    active_workers: int

    idle_workers: int

    processing_requests: int

    queued_requests: int

    running_workers: int

    supported_inference: List[str]

    throttled_workers: int

    unhealthy_workers: int


class OmnistackDeployedModels(BaseModel):
    available_stats: List[str]

    last_updated: datetime

    api_model_type: Literal["omnistack_deployed_models"] = FieldInfo(alias="model_type")

    omni_model_id: str

    stats: Optional[OmnistackDeployedModelsStats] = None

    status: Literal["normal", "failed", "warning", "throttled"]


ModelsDashboardOverviewRetrieveResponse: TypeAlias = Union[ExternalModelConnectionsStatus, OmnistackDeployedModels]
