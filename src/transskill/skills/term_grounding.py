"""Fixed specification for terminology grounding and localization."""

from transskill.schemas import Phenomenon

from .base import SkillSpec


class TermGroundingAndLocalizationSkill:
    spec = SkillSpec(
        phenomenon=Phenomenon.TERMINOLOGY_LOCALIZATION,
        skill_name="Term Grounding and Localization",
        objective="Ground the source concept before choosing an accurate, genre-appropriate English form.",
        required_decision_fields=[
            "term", "grounded_concept", "term_type", "narrative_role", "relevant_attributes",
            "established_rendering", "localization_strategy", "proposed_english_form",
        ],
        semantic_memory_requirement="primary",
        evidence_policy=(
            "Working Memory provides the current source, context, draft, and verified decisions. "
            "Episodic Memory provides analogous prior cases. Semantic Memory may provide reusable "
            "terminological, cultural, genre, or established-usage knowledge when needed. Retrieved "
            "cases are precedent and never establish the current interpretation by themselves."
        ),
        decision_procedure=(
            "First determine concept identity, term type, narrative role, and relevant attributes; "
            "then decide the English form using visible evidence of established usage. Do not invent "
            "worldbuilding or unsupported attributes."
        ),
        corrective_strategies=[
            "Use an established equivalent when supported by visible usage.",
            "Use semantic translation when it best preserves the grounded concept.",
            "Use transliteration when identity or naming function should be retained.",
            "Use a concise explanatory realization when necessary for intelligibility.",
        ],
        verification_criterion=(
            "The candidate preserves concept identity, relevant attributes, and narrative role, and "
            "any claimed established rendering is supported by visible usage."
        ),
    )
