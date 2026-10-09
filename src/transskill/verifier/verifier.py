"""Check the selected target and preservation of resolved phenomena."""
from transskill.llm.component import LLMComponent
from transskill.schemas import DiagnosisStatus, VerificationResult

class SharedVerifier(LLMComponent):
    def verify(self, state, step, execution, spec):
        result = self.request(
            "Verify whether the provisional decision is supported by the source and context "
            "and realized in the candidate draft. Check preservation of resolved phenomena.",
            {"state": state.model_dump(mode="json"), "step": step.model_dump(mode="json"),
             "execution": execution.model_dump(mode="json"),
             "skill": spec.model_dump(mode="json")}, VerificationResult,
        )
        if not any(item.status is DiagnosisStatus.RESOLVED for item in state.diagnosis.items):
            result.preservation_pass = True
        return result
