"""Diagnose every detected phenomenon in the current draft."""
from transskill.llm.component import LLMComponent
from transskill.llm.base import StructuredOutputError
from transskill.schemas import DiagnosisResult

class LLMMultiPhenomenonDiagnoser(LLMComponent):
    def diagnose(self, state):
        result = self.request(
            "Diagnose each detected phenomenon exactly once as resolved, unresolved, "
            "or undetermined. Provide corrective targets only for unresolved items.",
            state.model_dump(mode="json"), DiagnosisResult,
        )
        expected = set(state.detection.phenomena)
        received = [item.phenomenon for item in result.items]
        targets = [t.target_id for item in result.items for t in item.targets]
        if (result.sample_id != state.sample.sample_id or set(received) != expected
                or len(received) != len(set(received)) or len(targets) != len(set(targets))):
            raise StructuredOutputError("Diagnosis must match detected phenomena and unique targets")
        return result
