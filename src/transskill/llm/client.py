"""Test-only structured-output LLM client."""

from __future__ import annotations

from collections import deque
from collections.abc import Iterable
from typing import Any

from pydantic import ValidationError

from .base import LLMClient, StructuredModel, StructuredOutputError


MockResponse = str | dict[str, Any]


class MockLLMClient(LLMClient):
    """Returns registered JSON objects or dictionaries without network access."""

    def __init__(self, responses: Iterable[MockResponse] = ()) -> None:
        self._responses: deque[MockResponse] = deque(responses)

    def register(self, response: MockResponse) -> None:
        """Append one response to the FIFO response queue."""
        self._responses.append(response)

    def generate_structured(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        response_model: type[StructuredModel],
    ) -> StructuredModel:
        """Validate the next registered response; never return raw data."""
        del system_prompt, user_prompt
        if not self._responses:
            raise StructuredOutputError("MockLLMClient has no registered response")

        response = self._responses.popleft()
        try:
            if isinstance(response, str):
                return response_model.model_validate_json(response, strict=True)
            if isinstance(response, dict):
                return response_model.model_validate(response, strict=True)
        except ValidationError as error:
            raise StructuredOutputError("Invalid structured model output") from error

        raise StructuredOutputError("MockLLMClient responses must be JSON strings or dictionaries")
