"""Plan corrective operations against unresolved targets."""
from transskill.llm.component import LLMComponent
from transskill.llm.base import StructuredOutputError
from transskill.schemas import DiagnosisStatus, Plan

class DynamicPlanner(LLMComponent):
    def plan(self, state, registry):
        result = self.request(
            "Plan an ordered subset of unresolved targets using the supplied skill specs. "
            "The controller executes only the first step and then replans.",
            {"state": state.model_dump(mode="json"),
             "skills": [s.model_dump(mode="json") for s in registry.all()]}, Plan,
        )
        targets = {(t.phenomenon, t.target_id) for item in state.diagnosis.items
                   if item.status is DiagnosisStatus.UNRESOLVED for t in item.targets}
        selected = set()
        for step in result.steps:
            key = (step.phenomenon, step.target_id)
            if (key not in targets or key in selected
                    or step.skill_name != registry.get(step.phenomenon).skill_name):
                raise StructuredOutputError("Invalid planned target or skill")
            selected.add(key)
        return result
