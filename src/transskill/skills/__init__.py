"""Fixed translation skill specifications and registry."""

from .base import SkillSpec
from .cultural_safety import SafetyAwareCulturalAdaptationSkill
from .idiomatic_realization import IdiomaticRealizationSkill
from .referent_recovery import ReferentRecoverySkill
from .registry import DEFAULT_SKILL_REGISTRY, SkillRegistry
from .sense_resolution import SenseResolutionSkill
from .temporal_reconstruction import TemporalReconstructionSkill
from .term_grounding import TermGroundingAndLocalizationSkill

__all__ = [
    "DEFAULT_SKILL_REGISTRY",
    "IdiomaticRealizationSkill",
    "ReferentRecoverySkill",
    "SafetyAwareCulturalAdaptationSkill",
    "SenseResolutionSkill",
    "SkillRegistry",
    "SkillSpec",
    "TemporalReconstructionSkill",
    "TermGroundingAndLocalizationSkill",
]
