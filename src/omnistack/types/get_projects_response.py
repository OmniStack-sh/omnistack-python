# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["GetProjectsResponse", "CurrentDayCost"]


class CurrentDayCost(BaseModel):
    cost: float

    currency: str


class GetProjectsResponse(BaseModel):
    current_day_avg_latency: float

    current_day_cost: CurrentDayCost

    current_day_errors: int

    current_day_requests: int

    omni_model_id: str

    project_id: str

    project_name: str

    status: str
