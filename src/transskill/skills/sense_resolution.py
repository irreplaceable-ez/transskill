"""Fixed specification for lexical sense resolution."""

from transskill.schemas import Phenomenon

from .base import SkillSpec


class SenseResolutionSkill:
    spec = SkillSpec(
        phenomenon=Phenomenon.LEXICAL_AMBIGUITY,
        skill_name="Sense Resolution",
        objective="Correct an expression whose current English rendering conveys an unsupported sense.",
        required_decision_fields=[
            "ambiguous_unit", "candidate_senses", "selected_sense", "contextual_evidence",
            "prerequisite_interpretation", "proposed_realization",
        ],
        semantic_memory_requirement="optional",
        evidence_policy=(
            "Working Memory provides the current source, context, draft, and verified decisions. "
            "Episodic Memory provides analogous prior cases. Semantic Memory may provide reusable "
            "lexical, collocational, or genre knowledge when needed. Retrieved cases are precedent "
            "and never establish the current interpretation by themselves."
        ),
        decision_procedure=(
            "Enumerate plausible senses and compare them against syntax, collocation, speaker intent, "
            "and discourse. Select only a sense supported by the current context, respecting any "
            "verified prerequisite interpretation. Retrieved cases are precedent, not answers."
        ),
        corrective_strategies=[
            "Replace the unsupported lexical choice with a context-supported equivalent.",
            "Rephrase locally when no single English word preserves the selected sense.",
        ],
        verification_criterion="The selected sense is supported by context and realized in the candidate draft.",
    )
