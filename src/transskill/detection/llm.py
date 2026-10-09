"""Detect phenomena using source and context only."""
from transskill.llm.component import LLMComponent
from transskill.llm.base import StructuredOutputError
from transskill.schemas import DetectionResult, Phenomenon

class LLMPhenomenonDetector(LLMComponent):
    def detect(self, *, sample_id, source, context):
        result = self.request(
            "Detect applicable translation phenomena from source and context only: "
            + ", ".join(p.value for p in Phenomenon),
            {"sample_id": sample_id, "source": source, "context": context},
            DetectionResult,
        )
        if result.sample_id != sample_id:
            raise StructuredOutputError("Detection sample mismatch")
        return result
