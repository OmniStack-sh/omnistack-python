# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomModelFetchCustomModelResponse", "SupportedGPU"]


class SupportedGPU(BaseModel):
    id: str

    cpu: str = FieldInfo(alias="CPU")

    gpus: List[str] = FieldInfo(alias="GPUs")

    name: str

    price: float

    ram: int

    ram_bandwidth: float

    tokens_per_second: int


class CustomModelFetchCustomModelResponse(BaseModel):
    context_length: int

    inference_memory: float

    api_model_architectures: str = FieldInfo(alias="model_architectures")

    api_model_size: float = FieldInfo(alias="model_size")

    num_parameters: float

    readme: str

    supported_gpus: List[SupportedGPU]

    supported_inference: List[str]

    torch_dtype: str
