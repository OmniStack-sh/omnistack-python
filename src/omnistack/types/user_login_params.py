# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserLoginParams"]


class UserLoginParams(TypedDict, total=False):
    about_user: Optional[str]

    how_did_you_hear_about_us: Optional[str]
