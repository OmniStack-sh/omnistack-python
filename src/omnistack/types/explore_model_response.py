# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .proxy import Proxy
from .._models import BaseModel

__all__ = ["ExploreModelResponse", "Omnideploy", "SupportedProvider"]


class Omnideploy(BaseModel):
    api_model_description: str = FieldInfo(alias="model_description")

    api_model_type: str = FieldInfo(alias="model_type")

    provider_model_id: str

    provider_name: str

    readme: str


class SupportedProvider(BaseModel):
    api_model_type: str = FieldInfo(alias="model_type")

    provider_description: str

    provider_name: str

    readme: str


class ExploreModelResponse(BaseModel):
    omnideploy: List[Omnideploy]
    """The trending models available"""

    omniproxy: List[Proxy]
    """The proxy models available"""

    supported_providers: List[SupportedProvider]
    """The supported providers"""
