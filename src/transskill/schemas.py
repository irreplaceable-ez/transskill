"""Basic framework contracts; no dataset or experiment metadata."""
from __future__ import annotations
from enum import Enum
from typing import Any
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid")

class Phenomenon(str, Enum):
    """Translation phenomena supported by TransSkill."""

    IDIOM_TRANSLATION = "idiom_translation"
    LEXICAL_AMBIGUITY = "lexical_ambiguity"
    TERMINOLOGY_LOCALIZATION = "terminology_localization"
    TENSE_CONSISTENCY = "tense_consistency"
    ZERO_PRONOUN = "zero_pronoun"
    CULTURAL_SAFETY = "cultural_safety"

class DiagnosisStatus(str, Enum):
    """Outcome states for diagnosis items."""

    RESOLVED = "resolved"
    UNRESOLVED = "unresolved"
    UNDETERMINED = "undetermined"

class RevisionCase(Contract):
    """Reference-free case visible to the core translation revision pipeline."""

    model_config = ConfigDict(extra="forbid")

    sample_id: str
    source: str
    context: str | None = None

class DetectionResult(Contract):
    """Phenomena instantiated by a Chinese source and its narrative context."""

    sample_id: str
    phenomena: list[Phenomenon] = Field(default_factory=list, max_length=6)

    @field_validator("phenomena")
    @classmethod
    def phenomena_must_be_unique(cls, phenomena: list[Phenomenon]) -> list[Phenomenon]:
        if len(phenomena) != len(set(phenomena)):
            raise ValueError("phenomena must not contain duplicates")
        return phenomena

class DiagnosisTarget(Contract):
    """One minimal, coherent corrective decision unit for a phenomenon."""

    target_id: str
    phenomenon: Phenomenon
    source_span: str | None = None
    role: str | None = None
    description: str

class ProvisionalDecisionRecord(Contract):
    """Concise decision; evidence_ids are semantic-only, episodic IDs separate."""

    target_id: str
    phenomenon: Phenomenon
    skill_name: str
    selected_interpretation_or_decision: str | None
    supporting_evidence: str | list[str]
    prerequisite_decisions: list[str]
    realization_strategy: str
    proposed_edit: str
    evidence_ids: list[str] = Field(default_factory=list)
    episodic_evidence_ids: list[str] = Field(default_factory=list)
    details: dict[str, Any]

class PhenomenonDiagnosis(Contract):
    phenomenon: Phenomenon
    status: DiagnosisStatus
    targets: list[DiagnosisTarget] = Field(default_factory=list)
    explanation: str

    @model_validator(mode="after")
    def validate_targets(self):
        if (self.status is DiagnosisStatus.UNRESOLVED) != bool(self.targets):
            raise ValueError("Only unresolved diagnoses must have targets")
        if any(t.phenomenon != self.phenomenon for t in self.targets):
            raise ValueError("Target phenomenon mismatch")
        return self

class DiagnosisResult(Contract):
    sample_id: str
    items: list[PhenomenonDiagnosis] = Field(default_factory=list)

class PlanStep(Contract):
    target_id: str
    phenomenon: Phenomenon
    skill_name: str
    instruction: str

class Plan(Contract):
    steps: list[PlanStep] = Field(default_factory=list)

class ExecutionResult(Contract):
    candidate_draft: str
    provisional_decision: ProvisionalDecisionRecord

class VerificationResult(Contract):
    target_pass: bool
    preservation_pass: bool
    feedback: str

class AttemptRecord(Contract):
    step: PlanStep
    execution: ExecutionResult
    verification: VerificationResult
    committed: bool

class WorkingState(Contract):
    sample: RevisionCase
    initial_draft: str
    committed_draft: str
    detection: DetectionResult | None = None
    diagnosis: DiagnosisResult | None = None
    verified_decisions: list[ProvisionalDecisionRecord] = Field(default_factory=list)
    attempts: list[AttemptRecord] = Field(default_factory=list)

class EpisodeRecord(Contract):
    working_state: WorkingState
    termination_reason: str
