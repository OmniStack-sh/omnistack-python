# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["CreatePromptResponse"]


class CreatePromptResponse(BaseModel):
    commit_date: datetime

    commit_message: str

    commit_version: str
