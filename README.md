# NexPilot Mini

An early Python prototype exploring asynchronous task orchestration, typed task models, logging, and service boundaries for a repository/documentation assistant.

> **Status: experimental scaffold, not a functioning autonomous coding agent.** The current service functions are stubs that simulate work and return placeholder results. Repository inspection and documentation retrieval are not implemented yet.

## Current structure

- `app/models.py` — Pydantic task and task-result models with status values.
- `app/config.py` — environment-based settings using Pydantic Settings.
- `app/services.py` — asynchronous placeholder functions for repository analysis and documentation search.
- `app/main.py` — small async demonstration that runs the service stubs concurrently and logs errors.
- `app/exceptions.py` — custom service exceptions.

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt`

## Setup

```bash
git clone https://github.com/Xatreus/nexpilot-mini.git
cd nexpilot-mini
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies and run the current demonstration:

```bash
python -m pip install -r requirements.txt
python app/main.py
```

The demo intentionally calls placeholder services with invalid sample inputs to exercise exception handling. It does not connect to GitHub, search external documentation, call an LLM, or make code changes.

## Next milestones

- Implement validated GitHub repository URL parsing and read-only repository inspection.
- Add real documentation search with source links.
- Define explicit tool contracts and structured task results.
- Add unit tests for successful paths, error handling, and invalid input.
- Add secret-safe configuration examples and CI.

## License

No license is currently declared. Until a license is added, assume standard copyright applies.
