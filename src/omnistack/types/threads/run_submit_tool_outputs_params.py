# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RunSubmitToolOutputsParams", "ToolOutput"]


class RunSubmitToolOutputsParams(TypedDict, total=False):
    thread_id: Required[str]

    tool_outputs: Required[Iterable[ToolOutput]]
    """A list of tools for which the outputs are being submitted."""

    stream: Optional[bool]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


class ToolOutput(TypedDict, total=False):
    output: str
    """The output of the tool call to be submitted to continue the run."""

    tool_call_id: str
    """
    The ID of the tool call in the `required_action` object within the run object
    the output is being submitted for.
    """
