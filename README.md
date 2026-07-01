# Template Project: GraphQL (Strawberry) + SQLAlchemy + FastAPI

Quick implementation of a database connector with both REST endpoints and GraphQL routes.

---

## Requirements

| Tool   | Version                                       |
|--------|-----------------------------------------------|
| Python | >= 3.12                                       |
| uv     | latest                                        |
| just   | latest (optional, for the `justfile` recipes) |

## Initialization

1. Clone the repository:
    ```bash
    git clone https://github.com/Cybernetic-Ransomware/template_GraphQL_SQLAlchemy_FastAPI.git
    ```
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
3. Install dependencies (creates `.venv` and installs runtime + dev dependencies):
    ```bash
    uv sync
    ```
4. Run the application:
    ```bash
    uv run uvicorn app.main:app --reload --port 8080
    ```
    or, with [just](https://github.com/casey/just):
    ```bash
    just run
    ```

---

## Default Checkups

- OpenAPI Documentation: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- GraphQL Playground: [http://127.0.0.1:8080/graphql](http://127.0.0.1:8080/graphql)

---

## Database Backends

`DATABASE_URL` is read from `.env` (copy `.env.template` to get started). Supported modes:

| Mode | `DATABASE_URL` example | Account required | Best for |
|---|---|---|---|
| Plain SQLite | `sqlite:///./test.db` | No | Local dev, CI (default) |
| Local libSQL | `sqlite+libsql:///local.db` | No | Trying the libSQL driver without a cloud account |
| Turso remote | `sqlite+libsql://<db>.turso.io?secure=true` | Yes | Serverless/multi-instance deployments |
| Turso embedded replica | `sqlite+libsql:///embedded.db` + `TURSO_DATABASE_URL` | Yes | Low-latency local reads, synced to the cloud |
| Native Turso (bonus) | `sqlite+turso:///local_native.db` | No | Experimental — unrelated to Turso Cloud/libSQL |

Only the plain SQLite mode runs in CI/tests; the others need real Turso credentials
(`turso db tokens create <name>`) and are for manual/local use.

---

## Development

Set up the pre-commit hooks once after cloning:
```bash
uv run pre-commit install
```

Common tasks (see `justfile` for the full list):
```bash
just format   # ruff format
just lint     # ruff format + lint, ty type-check, codespell, bandit
just commit   # run pre-commit, then open Commitizen for a conventional commit
```

---

## Useful links and documentation

- SQLAlchemy: [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)
- FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Strawberry GraphQL: [https://strawberry.rocks/docs](https://strawberry.rocks/docs)
