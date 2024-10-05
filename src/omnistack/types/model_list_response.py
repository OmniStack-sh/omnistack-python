# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModelListResponse",
    "ModelListResponseItem",
    "ModelListResponseItemAppSchemasEndpointsModelsModelsExternalModelStats",
    "ModelListResponseItemAppSchemasEndpointsModelsModelsExternalModelStatsCurrentDayCost",
    "ModelListResponseItemAppSchemasEndpointsModelsModelsOmnistackDeployedModelsStats",
    "ModelListResponseItemAppSchemasEndpointsModelsModelsOmnistackDeployedModelsStatsCurrentDayCost",
]


class ModelListResponseItemAppSchemasEndpointsModelsModelsExternalModelStatsCurrentDayCost(BaseModel):
    cost: float

    currency: str


class ModelListResponseItemAppSchemasEndpointsModelsModelsExternalModelStats(BaseModel):
    current_day_cost: ModelListResponseItemAppSchemasEndpointsModelsModelsExternalModelStatsCurrentDayCost

    current_day_requests: int

    last_updated: datetime

    api_model_id: str = FieldInfo(alias="model_id")

    api_model_type: Literal["external_model_connections", "proxy_models"] = FieldInfo(alias="model_type")

    omni_model_id: str

    provider_name: str

    remaining_requests: int

    remaining_tokens: int

    status: str


class ModelListResponseItemAppSchemasEndpointsModelsModelsOmnistackDeployedModelsStatsCurrentDayCost(BaseModel):
    cost: float

    currency: str


class ModelListResponseItemAppSchemasEndpointsModelsModelsOmnistackDeployedModelsStats(BaseModel):
    active_workers: int

    current_day_cost: ModelListResponseItemAppSchemasEndpointsModelsModelsOmnistackDeployedModelsStatsCurrentDayCost

    current_day_requests: int

    api_model_id: str = FieldInfo(alias="model_id")

    api_model_type: Literal["omnistack_deployed_models"] = FieldInfo(alias="model_type")

    omni_model_id: str

    provider_name: str

    queued_requests: int

    status: str


ModelListResponseItem: TypeAlias = Union[
    ModelListResponseItemAppSchemasEndpointsModelsModelsExternalModelStats,
    ModelListResponseItemAppSchemasEndpointsModelsModelsOmnistackDeployedModelsStats,
]

ModelListResponse: TypeAlias = List[ModelListResponseItem]
