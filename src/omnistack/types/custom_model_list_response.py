# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CustomModelListResponse"]


class CustomModelListResponse(BaseModel):
    readme: str

    required_params: List[str]
