"""Basic bounded detect-diagnose-plan-execute-verify loop."""
from transskill.schemas import (
    AttemptRecord, DiagnosisStatus, EpisodeRecord, RevisionCase, WorkingState,
)

class TransSkillController:
    def __init__(self, *, detector, diagnoser, planner, executor, verifier, registry, max_steps=3):
        if isinstance(max_steps, bool) or not isinstance(max_steps, int) or max_steps < 0:
            raise ValueError("max_steps must be a non-negative integer")
        self.detector, self.diagnoser, self.planner = detector, diagnoser, planner
        self.executor, self.verifier, self.registry = executor, verifier, registry
        self.max_steps = max_steps

    def run(self, sample: RevisionCase, *, initial_draft: str) -> EpisodeRecord:
        if not isinstance(sample, RevisionCase):
            raise TypeError("Expected a reference-free RevisionCase")
        state = WorkingState(sample=sample, initial_draft=initial_draft, committed_draft=initial_draft)
        state.detection = self.detector.detect(
            sample_id=sample.sample_id, source=sample.source, context=sample.context or "",
        )
        state.diagnosis = self.diagnoser.diagnose(state.model_copy(deep=True))
        while True:
            actionable = [i for i in state.diagnosis.items if i.status is DiagnosisStatus.UNRESOLVED]
            if not actionable:
                reason = ("blocked_by_uncertainty" if any(
                    i.status is DiagnosisStatus.UNDETERMINED for i in state.diagnosis.items
                ) else "all_resolved")
                break
            if len(state.attempts) >= self.max_steps:
                reason = "budget_exhausted"
                break
            plan = self.planner.plan(state.model_copy(deep=True), self.registry)
            if not plan.steps:
                reason = "empty_plan"
                break
            step = plan.steps[0]
            spec = self.registry.get(step.phenomenon)
            execution = self.executor.execute(state.model_copy(deep=True), step, spec)
            verification = self.verifier.verify(state.model_copy(deep=True), step, execution, spec)
            committed = verification.target_pass and verification.preservation_pass
            state.attempts.append(AttemptRecord(
                step=step, execution=execution, verification=verification, committed=committed,
            ))
            if committed:
                state.committed_draft = execution.candidate_draft
                state.verified_decisions.append(execution.provisional_decision)
                state.diagnosis = self.diagnoser.diagnose(state.model_copy(deep=True))
        return EpisodeRecord(working_state=state, termination_reason=reason)
