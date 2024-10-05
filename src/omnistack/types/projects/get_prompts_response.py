# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GetPromptsResponse"]


class GetPromptsResponse(BaseModel):
    created_at: datetime

    description: str

    name: str

    prompt_id: str

    status: Literal["active", "complete", "incomplete"]

    type: List[Literal["chat", "completion"]]
