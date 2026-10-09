"""Fixed skill specification for zero-pronoun referent recovery."""

from .base import SkillSpec
from transskill.schemas import Phenomenon


class ReferentRecoverySkill:
    """Declarative skill only; it has no model calls or state mutations."""

    spec = SkillSpec(
        phenomenon=Phenomenon.ZERO_PRONOUN,
        skill_name="Referent Recovery",
        objective=(
            "Recover omitted arguments and preserve who performs or undergoes the source event "
            "in a natural English realization."
        ),
        required_decision_fields=[
            "elliptical_position",
            "grammatical_role",
            "candidate_antecedents",
            "selected_referent",
            "discourse_evidence",
            "person_number",
            "proposed_realization",
        ],
        semantic_memory_requirement="not_required",
        evidence_policy=(
            "Working Memory provides the current source, context, draft, and verified decisions. "
            "Episodic Memory provides analogous prior cases. Semantic Memory may provide reusable "
            "linguistic or discourse knowledge when needed. Retrieved cases are precedent and "
            "never establish the current interpretation by themselves. Gender is optional evidence "
            "and may be used only when supported."
        ),
        decision_procedure=(
            "Locate the elliptical position and grammatical role; compare candidate antecedents "
            "using grammatical role, discourse continuity, semantic compatibility, and speaker "
            "perspective. Recency alone is insufficient. Select person and number from evidence, "
            "then choose a natural realization. Referent Recovery does not require an overt pronoun "
            "when a natural target construction already conveys the referent adequately. A clause "
            "that is structurally incomplete because a required English subject or object is missing "
            "still requires repair."
        ),
        corrective_strategies=[
            "Use a contextually supported pronoun.",
            "Use a name or noun phrase when that is clearer or grammatically appropriate.",
            "Restructure the clause when English can naturally preserve the referent without an overt pronoun.",
        ],
        verification_criterion=(
            "The selected entity fits the grammatical role; who performs or undergoes the event is "
            "preserved; person and number are consistent; and the realization is grammatically natural."
        ),
    )
