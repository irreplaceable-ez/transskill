# TransSkill Basic Framework 

## Layout

- `src/transskill/schemas.py`: basic input, diagnosis, plan, execution, verification, and state contracts.
- `src/transskill/controller.py`: bounded revision loop.
- `src/transskill/runner.py`: assembly entry point, `run_episode(...)`.
- `src/transskill/detection/`, `diagnosis/`, `planner/`, `executor/`, `verifier/`: basic components.
- `src/transskill/skills/`: six fixed skill specifications and registry.
- `src/transskill/llm/`: structured model interface and offline client with an empty response queue.
- `src/transskill/memory/`: empty memory interfaces.
- `configs/framework.example.yaml`: settings documentation and commented configuration placeholders.

## Usage

Install from this directory:

```bash
python -m pip install -e .
```

Call `transskill.runner.run_episode` with explicit `source`, `context`,
`initial_draft`, `sample_id`, `llm_client`, and optional `max_steps` arguments.
It returns an `EpisodeRecord`. The framework does not automatically read data,
connect to services, or write files.

Each component makes a single structured-output call. Validation failures raise
errors directly. The controller executes only the first planned step per iteration
and commits a candidate draft only when both target and preservation checks pass.
Rejected revisions leave the committed draft unchanged.


