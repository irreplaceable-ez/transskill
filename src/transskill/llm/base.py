"""Structured-output LLM interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar

from pydantic import BaseModel


StructuredModel = TypeVar("StructuredModel", bound=BaseModel)


class StructuredOutputError(ValueError):
    """Raised when a model response cannot satisfy its declared schema."""


class LLMClient(ABC):
    """Synchronous client contract for validated structured model output."""

    @abstractmethod
    def generate_structured(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        response_model: type[StructuredModel],
    ) -> StructuredModel:
        """Generate and validate one response against ``response_model``."""
        raise NotImplementedError
