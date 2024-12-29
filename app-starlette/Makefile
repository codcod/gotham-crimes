.PHONY: run dev .http
.PHONY: .fmt .pre-commit .bandit
.PHONY: .db .wrk .gha

export PYTHONPATH=src

HOST = 127.0.0.1
PORT = 8000

# --- run server

run:
	./.venv/bin/uvicorn crimes.app:app \
		--workers 8 \
		--log-level warning

dev:
	./.venv/bin/uvicorn crimes.app:app \
		--reload \
		--log-level debug

# --- interact with the app

test:
	uv run pytest

# --- work with code

.fmt:
	uvx ruff format
	uvx ruff check --fix
#    uv run mypy --strict --scripts-are-modules src

.bandit:
	uv run -- bandit -c pyproject.toml -r .

# --- prepare & build

.db:
	uv run -- python src/crimes/models.py

run/infra:
	COMPOSE_PROFILES=infra docker compose up -d

stop/infra:
	COMPOSE_PROFILES=infra docker compose down

clean:
	rm -rf .docker-data || true

.gha:
	act -W '.github/workflows/ci.yml'
