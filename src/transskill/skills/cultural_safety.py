"""Fixed specification for safety-aware cultural adaptation."""

from transskill.schemas import Phenomenon

from .base import SkillSpec


class SafetyAwareCulturalAdaptationSkill:
    spec = SkillSpec(
        phenomenon=Phenomenon.CULTURAL_SAFETY,
        skill_name="Safety-aware Cultural Adaptation",
        objective=(
            "Repair translation-induced distortion of culturally sensitive meaning while preserving "
            "fidelity, attribution, and discourse function."
        ),
        required_decision_fields=[
            "sensitive_expression", "source_meaning", "attribution", "discourse_function",
            "contextual_or_cultural_evidence", "draft_distortion", "editorial_criterion",
            "adaptation_strategy",
        ],
        semantic_memory_requirement="enabled",
        evidence_policy=(
            "Working Memory provides the current source, context, draft, and verified decisions. "
            "Episodic Memory provides analogous prior cases. Semantic Memory may provide reusable "
            "cultural, pragmatic, or safety knowledge when needed. Retrieved cases are precedent and "
            "never establish the current interpretation by themselves. Any additional editorial "
            "criterion must be recorded explicitly."
        ),
        decision_procedure=(
            "Sensitive source content itself is not an error; identify translation-induced distortion. "
            "Preserve attribution, speaker attitude, and discourse function. Do not silently remove "
            "source events, reverse speaker attitude, turn quoted prejudice into narrator endorsement, "
            "or soften source content merely because it is uncomfortable. Record any additional "
            "editorial criterion explicitly before adaptation."
        ),
        corrective_strategies=[
            "Restore faithful attribution and discourse framing.",
            "Use safety-aware wording that preserves source meaning without unsupported distortion.",
            "Apply an explicit editorial criterion only when one has been supplied and recorded.",
        ],
        verification_criterion=(
            "The candidate preserves fidelity, attribution, and discourse function while satisfying "
            "the applicable and explicitly recorded appropriateness criterion."
        ),
    )
