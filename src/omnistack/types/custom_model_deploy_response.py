# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["CustomModelDeployResponse"]


class CustomModelDeployResponse(BaseModel):
    deployment_id: str

    status: str
