# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .model_provider_details import ModelProviderDetails

__all__ = ["ConnectListResponse"]

ConnectListResponse: TypeAlias = List[ModelProviderDetails]
