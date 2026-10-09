"""Shared single-call helper for framework components."""
import json
from transskill.llm.base import StructuredOutputError

class LLMComponent:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def request(self, instruction, payload, response_model):
        result = self.llm_client.generate_structured(
            system_prompt=instruction,
            user_prompt=json.dumps(payload, ensure_ascii=False),
            response_model=response_model,
        )
        if not isinstance(result, response_model):
            raise StructuredOutputError("Unexpected response type")
        return result
