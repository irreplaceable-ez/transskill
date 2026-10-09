"""Fixed specification for temporal reconstruction."""

from transskill.schemas import Phenomenon

from .base import SkillSpec


class TemporalReconstructionSkill:
    spec = SkillSpec(
        phenomenon=Phenomenon.TENSE_CONSISTENCY,
        skill_name="Temporal Reconstruction",
        objective="Reconstruct source temporal relations as coherent English tense and aspect choices.",
        required_decision_fields=[
            "target_event", "temporal_anchors", "event_relations", "reference_point",
            "narrative_frame", "viewpoint", "selected_tense_aspect", "prerequisite_decision",
        ],
        semantic_memory_requirement="not_required",
        evidence_policy=(
            "Working Memory provides the current source, context, draft, and verified decisions. "
            "Episodic Memory provides analogous prior cases. Semantic Memory may provide reusable "
            "tense, aspect, discourse, or genre knowledge when needed. Retrieved cases are precedent "
            "and never establish the current interpretation by themselves."
        ),
        decision_procedure=(
            "Separate source temporal meaning from assumptions introduced by the draft. Identify "
            "anchors, event relations, reference point, narrative frame, and viewpoint. Treat verified "
            "lexical or referential decisions as possible prerequisites. Do not globally normalize all "
            "verbs to one tense."
        ),
        corrective_strategies=[
            "Adjust tense or aspect locally to express the supported event relation.",
            "Restructure temporal subordination or sequencing when morphology alone is insufficient.",
        ],
        verification_criterion=(
            "The candidate preserves event ordering, duration, completion, habituality, viewpoint, "
            "and the narrative temporal frame."
        ),
    )
