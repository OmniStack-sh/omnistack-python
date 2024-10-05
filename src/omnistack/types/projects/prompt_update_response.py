# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .create_prompt_response import CreatePromptResponse

__all__ = ["PromptUpdateResponse"]

PromptUpdateResponse: TypeAlias = List[CreatePromptResponse]
