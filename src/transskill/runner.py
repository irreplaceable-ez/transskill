"""Assemble the basic framework with a caller-supplied LLM client."""
from transskill.controller import TransSkillController
from transskill.detection.llm import LLMPhenomenonDetector
from transskill.diagnosis.multi import LLMMultiPhenomenonDiagnoser
from transskill.executor.executor import SharedExecutor
from transskill.planner.planner import DynamicPlanner
from transskill.schemas import RevisionCase
from transskill.skills.registry import SkillRegistry
from transskill.verifier.verifier import SharedVerifier

def run_episode(*, source, context, initial_draft, sample_id, llm_client, max_steps=3):
    controller = TransSkillController(
        detector=LLMPhenomenonDetector(llm_client),
        diagnoser=LLMMultiPhenomenonDiagnoser(llm_client),
        planner=DynamicPlanner(llm_client), executor=SharedExecutor(llm_client),
        verifier=SharedVerifier(llm_client), registry=SkillRegistry(), max_steps=max_steps,
    )
    return controller.run(
        RevisionCase(sample_id=sample_id, source=source, context=context), initial_draft=initial_draft,
    )
