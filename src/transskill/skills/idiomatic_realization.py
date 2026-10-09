"""Fixed specification for idiomatic realization."""

from transskill.schemas import Phenomenon

from .base import SkillSpec


class IdiomaticRealizationSkill:
    spec = SkillSpec(
        phenomenon=Phenomenon.IDIOM_TRANSLATION,
        skill_name="Idiomatic Realization",
        objective="Repair loss or distortion of figurative meaning, pragmatic function, register, or force.",
        required_decision_fields=[
            "source_expression", "contextual_meaning", "pragmatic_function", "register_or_force",
            "speaker_stance", "realization_strategy", "proposed_wording",
        ],
        semantic_memory_requirement="enabled",
        evidence_policy=(
            "Working Memory provides the current source, context, draft, and verified decisions. "
            "Episodic Memory provides analogous prior cases. Semantic Memory may provide reusable "
            "idiomatic, pragmatic, or register knowledge when needed. Retrieved cases are precedent "
            "and never establish the current interpretation by themselves."
        ),
        decision_procedure=(
            "Establish contextual figurative meaning, pragmatic function, register, force, and speaker "
            "stance before selecting an English strategy. An adequate English paraphrase does not "
            "require replacement merely because it is not itself an idiom."
        ),
        corrective_strategies=[
            "Use a functionally equivalent English idiom when context and register support it.",
            "Use a natural paraphrase that preserves meaning and communicative force.",
            "Retain imagery selectively when it remains intelligible and appropriate.",
        ],
        verification_criterion=(
            "The candidate preserves contextual meaning, communicative force, speaker stance, and register."
        ),
    )
