# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserRetrieveResponse", "Workspace"]


class Workspace(BaseModel):
    name: str

    workspace_id: str


class UserRetrieveResponse(BaseModel):
    account_status: Literal["incomplete", "stripe_pending", "complete", "unregistered"]

    required_params: Optional[List[str]] = None

    workspaces: Optional[List[Workspace]] = None
