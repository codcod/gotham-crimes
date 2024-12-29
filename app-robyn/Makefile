.PHONY: run dev .http
.PHONY: .fmt .pre-commit .bandit
.PHONY: .db .wrk .gha

export PYTHONPATH=.

HOST = 127.0.0.1
PORT = 8000

# --- run server

run:
	./.venv/bin/robyn crimes/app.py \
	    --fast \
		--processes 2 \
		--workers 2 \
		--disable-openapi

dev:
	./.venv/bin/robyn crimes/app.py \
		--dev \
		--log-level DEBUG

# --- interact with the app

test:
	uv run pytest

# --- work with code

.fmt:
	uvx ruff format
	uvx ruff check --fix

.bandit:
	uv run -- bandit -c pyproject.toml -r .

# --- prepare & build

.db:
	uv run -- python src/models.py

run/infra:
	COMPOSE_PROFILES=infra docker compose up -d

stop/infra:
	COMPOSE_PROFILES=infra docker compose down

clean:
	rm -rf .docker-data || true

.gha:
	act -W '.github/workflows/ci.yml'
