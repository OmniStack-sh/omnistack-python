# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["BasicStats", "TotalCost"]


class TotalCost(BaseModel):
    cost: float

    currency: str


class BasicStats(BaseModel):
    total_cost: TotalCost

    total_errors: int

    total_requests: int

    total_tokens: int
