# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserLoginResponse"]


class UserLoginResponse(BaseModel):
    account_status: Literal["incomplete", "stripe_pending", "complete", "unregistered"]

    required_params: List[str]

    promo_offers: Optional[int] = None
