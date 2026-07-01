# 1. SQLite vs Turso vs Postgres for a small application

## Status

Accepted

## Context

This template is a single-process, low-traffic educational service (one `items` table, no
concurrent-write requirements). We need a storage choice that stays simple by default but has a
clear upgrade path if the project grows. Three realistic candidates:

- **SQLite** — embedded, file-based, zero ops.
- **Turso/libSQL** — SQLite-compatible, adds optional cloud replication (remote or
  embedded-replica modes) via `sqlalchemy-libsql`.
- **Postgres** — traditional client-server RDBMS.

## Decision

Keep **SQLite** as the default (`sqlite:///./test.db`), and support **Turso/libSQL** as a
configurable alternative (see README "Database Backends"). Do not adopt Postgres for this
template.

Rationale:

- SQLite has no operational overhead and no network hop, but a single file means no
  multi-instance/multi-writer story and file-locking limits under concurrent writes.
- Turso/libSQL keeps SQLite's simplicity (still a local file, same SQL dialect) while adding
  opt-in replication — a reasonable next step for read scaling or edge deployment without
  running a separate database server. Trade-offs: smaller ecosystem than Postgres, vendor
  dialect, Linux/macOS only.
- Postgres offers the best concurrent-write and relational-feature story, but requires running
  and operating a separate server — not justified while the schema is one table with no
  multi-writer traffic.

## Consequences

`DATABASE_URL` stays the single configuration knob (`app/core/config.py`), with a small amount of
driver-specific branching in `app/db/database.py`. If this template ever needs real multi-writer
concurrency or relational features beyond what SQLite/Turso comfortably support, that's the
trigger to revisit this decision and adopt Postgres.
