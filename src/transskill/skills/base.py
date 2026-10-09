"""Immutable specifications for fixed translation skills."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from transskill.schemas import Phenomenon


class SkillSpec(BaseModel):
    """Declarative, immutable contract for a non-agent translation skill."""

    model_config = ConfigDict(frozen=True)

    phenomenon: Phenomenon
    skill_name: str
    objective: str
    decision_procedure: str
    evidence_policy: str
    corrective_strategies: list[str] = Field(min_length=1)
    verification_criterion: str
    required_decision_fields: list[str] = Field(min_length=1)
    semantic_memory_requirement: Literal[
        "primary", "enabled", "optional", "not_required"
    ]

    @field_validator(
        "skill_name",
        "objective",
        "decision_procedure",
        "evidence_policy",
        "verification_criterion",
    )
    @classmethod
    def text_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("skill specification text must not be blank")
        return value

    @field_validator("corrective_strategies", "required_decision_fields")
    @classmethod
    def list_entries_must_not_be_blank(cls, values: list[str]) -> list[str]:
        if any(not value.strip() for value in values):
            raise ValueError("skill specification list entries must not be blank")
        if len(values) != len(set(values)):
            raise ValueError("skill specification list entries must be unique")
        return values

