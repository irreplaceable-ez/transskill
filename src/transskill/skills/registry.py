"""Strict registry of the six fixed TransSkill specifications."""

from collections.abc import Sequence

from transskill.schemas import Phenomenon

from .base import SkillSpec
from .cultural_safety import SafetyAwareCulturalAdaptationSkill
from .idiomatic_realization import IdiomaticRealizationSkill
from .referent_recovery import ReferentRecoverySkill
from .sense_resolution import SenseResolutionSkill
from .temporal_reconstruction import TemporalReconstructionSkill
from .term_grounding import TermGroundingAndLocalizationSkill


_FIXED_SPECS = (
    IdiomaticRealizationSkill.spec,
    SenseResolutionSkill.spec,
    TermGroundingAndLocalizationSkill.spec,
    TemporalReconstructionSkill.spec,
    ReferentRecoverySkill.spec,
    SafetyAwareCulturalAdaptationSkill.spec,
)

class SkillRegistry:
    """Provides exact lookup over the six supported phenomena with no fallback."""

    def __init__(self, specs: Sequence[SkillSpec] = _FIXED_SPECS) -> None:
        phenomena = [spec.phenomenon for spec in specs]
        if len(phenomena) != len(set(phenomena)):
            raise ValueError("SkillRegistry cannot contain duplicate phenomena")
        expected = set(Phenomenon)
        received = set(phenomena)
        if received != expected:
            raise ValueError(
                "SkillRegistry must contain exactly the six supported phenomena: "
                f"expected={sorted(item.value for item in expected)!r} "
                f"received={sorted(item.value for item in received)!r}"
            )
        self._specs = {spec.phenomenon: spec for spec in specs}

    def get(self, phenomenon: Phenomenon) -> SkillSpec:
        """Return the exact matching specification; unsupported values raise ``KeyError``."""
        try:
            return self._specs[phenomenon]
        except (KeyError, TypeError) as error:
            raise KeyError(f"Unsupported phenomenon: {phenomenon!r}") from error

    def all(self) -> Sequence[SkillSpec]:
        """Return all six specifications in canonical phenomenon order."""
        return tuple(self._specs[phenomenon] for phenomenon in Phenomenon)

DEFAULT_SKILL_REGISTRY = SkillRegistry()
