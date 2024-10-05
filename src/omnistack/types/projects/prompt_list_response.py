# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .get_prompts_response import GetPromptsResponse

__all__ = ["PromptListResponse"]

PromptListResponse: TypeAlias = List[GetPromptsResponse]
