# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "GetPromptResponse",
    "Prompt",
    "PromptPromptCommits",
    "PromptPromptCommitsSettings",
    "PromptPromptCommitsSettingsPlaygroundCompletionSettings",
    "PromptPromptCommitsSettingsPlaygroundChatSettings",
]


class PromptPromptCommitsSettingsPlaygroundCompletionSettings(BaseModel):
    frequency_penalty: Optional[float] = None
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.

    [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
    """

    max_tokens: Optional[int] = None
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the
    completion.

    The token count of your prompt plus `max_tokens` cannot exceed the model's
    context length.
    [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
    for counting tokens.
    """

    presence_penalty: Optional[float] = None
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.

    [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
    """

    stop: Union[str, List[str], None] = None
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: Optional[bool] = None
    """Whether to stream back partial progress.

    If set, tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).
    """

    temperature: Optional[float] = None
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.

    We generally recommend altering this or `top_p` but not both.
    """

    top_p: Optional[float] = None
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """


class PromptPromptCommitsSettingsPlaygroundChatSettings(BaseModel):
    frequency_penalty: Optional[float] = None
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.

    [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
    """

    max_tokens: Optional[int] = None
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the chat
    completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
    for counting tokens.
    """

    presence_penalty: Optional[float] = None
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.

    [See more information about frequency and presence penalties.](/docs/guides/text-generation/parameter-details)
    """

    stop: Union[str, List[str], None] = None
    """Up to 4 sequences where the API will stop generating further tokens."""

    stream: Optional[bool] = None
    """If set, partial message deltas will be sent, like in ChatGPT.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).
    """

    temperature: Optional[float] = None
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.

    We generally recommend altering this or `top_p` but not both.
    """

    top_p: Optional[float] = None
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """


PromptPromptCommitsSettings: TypeAlias = Union[
    PromptPromptCommitsSettingsPlaygroundCompletionSettings, PromptPromptCommitsSettingsPlaygroundChatSettings
]


class PromptPromptCommits(BaseModel):
    commit_message: str

    settings: Optional[Dict[str, PromptPromptCommitsSettings]] = None

    type: Optional[List[Literal["chat", "completion"]]] = None


class Prompt(BaseModel):
    created_at: datetime

    prompt_commits: PromptPromptCommits

    version_number: str


class GetPromptResponse(BaseModel):
    active_prompt_version: str

    description: str

    name: str

    prompts: Optional[List[Prompt]] = None

    status: Literal["active", "complete", "incomplete"]

    type: List[Literal["chat", "completion"]]

    updated_at: datetime
