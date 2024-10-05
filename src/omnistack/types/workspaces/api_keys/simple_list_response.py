# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["SimpleListResponse", "SimpleListResponseItem"]


class SimpleListResponseItem(BaseModel):
    id: str

    access_type: Literal["MODEL", "PLATFORM"]

    api_key_name: str

    api_type: Literal["simple"]

    created_at: datetime

    status: Literal["active", "deleted"]


SimpleListResponse: TypeAlias = List[SimpleListResponseItem]
