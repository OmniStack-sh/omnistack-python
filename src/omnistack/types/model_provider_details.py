# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ModelProviderDetails"]


class ModelProviderDetails(BaseModel):
    id: str

    provider_name: str

    readme: str

    required_params: List[str]
