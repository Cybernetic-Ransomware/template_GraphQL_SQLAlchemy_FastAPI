# Install/sync all dependencies (runtime + dev)
install:
    uv sync

# Apply ruff formatting to app source
format:
    uv run ruff format app/

# Run the full linting suite: format, lint, type-check, spell-check, security scan
lint:
    uv run ruff format app/
    uv run ruff check --fix app/
    uv run ty check
    uv run python -m codespell_lib app/
    uv run bandit -q -c pyproject.toml -r app/

# Run the test suite (plain SQLite mode only)
test:
    uv run pytest

# Run the app locally with auto-reload
# Swagger UI: http://127.0.0.1:8080/docs
# GraphQL Playground: http://127.0.0.1:8080/graphql
run:
    uv run uvicorn app.main:app --reload --port 8080

# Run pre-commit on staged files, then open Commitizen
commit:
    uv run pre-commit run
    uv run cz commit

# Bump version (auto-tags vX.Y.Z, updates pyproject.toml)
bump:
    uv run cz bump
