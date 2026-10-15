# Contributing

## Setup

```sh
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install             # optional
```

## Checks

```sh
ruff check .
ruff format --check .
pytest -q
```

CI runs the same three commands on Python 3.11 through 3.13.

## Layout

| Path | Contents |
|---|---|
| `src/emergent_mind/envs` | Partially observable multi-agent environments |
| `src/emergent_mind/agents` | Agent interface and implementations |
| `src/emergent_mind/memory` | Individual and shared memory stores |
| `src/emergent_mind/experiments` | Conditions, configs, and the episode runner |
| `src/emergent_mind/evaluation` | Metrics and probes |
| `docs/` | Research plan and design notes |
