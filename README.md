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

## Excluded Content

No datasets, samples, reference translations, annotations, knowledge bases,
experience records, model weights, results, logs, caches, virtual environments,
or version history are included.

Model-specific prompt addenda, sampling tuning, retries, truncation recovery,
output patches, retrieval ranking, frozen snapshots, development/test splits,
evaluation, ablation experiments, and cluster launch scripts have been removed.

Actual local paths, usernames, internal endpoints, and credentials are omitted,
including from comments. Local settings use commented generic placeholders for
project-relative paths or environment variable names.
