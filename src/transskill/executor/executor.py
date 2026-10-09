"""Propose one revision without committing state."""
from transskill.llm.component import LLMComponent
from transskill.llm.base import StructuredOutputError
from transskill.schemas import ExecutionResult

class SharedExecutor(LLMComponent):
    def execute(self, state, step, spec):
        result = self.request(
            "Apply only the selected target using the skill specification. Return a "
            "candidate draft and a supported provisional decision. Do not invent evidence.",
            {"state": state.model_dump(mode="json"), "step": step.model_dump(mode="json"),
             "skill": spec.model_dump(mode="json")}, ExecutionResult,
        )
        decision = result.provisional_decision
        if (decision.target_id != step.target_id or decision.phenomenon != step.phenomenon
                or decision.skill_name != spec.skill_name):
            raise StructuredOutputError("Decision must match selected target and skill")
        if decision.evidence_ids or decision.episodic_evidence_ids:
            raise StructuredOutputError("The framework ships with empty evidence stores")
        populated = decision.model_dump()
        populated.update(decision.details)
        if any(populated.get(field) in (None, "", [], {}) for field in spec.required_decision_fields):
            raise StructuredOutputError("Decision is missing required skill fields")
        return result
