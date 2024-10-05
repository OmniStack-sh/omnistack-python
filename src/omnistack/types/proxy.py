# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Proxy", "TokenCost", "TokenCostInputTokensCost", "TokenCostOutputTokensCost"]


class TokenCostInputTokensCost(BaseModel):
    cost: float

    currency: str


class TokenCostOutputTokensCost(BaseModel):
    cost: float

    currency: str


class TokenCost(BaseModel):
    input_tokens_cost: TokenCostInputTokensCost

    output_tokens_cost: TokenCostOutputTokensCost

    token_unit: float


class Proxy(BaseModel):
    context_window: int

    latency: int

    api_model_description: str = FieldInfo(alias="model_description")

    api_model_type: str = FieldInfo(alias="model_type")

    omniproxy_id: str

    provider_model_id: str

    provider_name: str

    readme: str

    supported_inference: List[str]

    token_cost: TokenCost

    tokens_per_second: int
