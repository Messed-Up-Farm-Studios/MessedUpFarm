SRC ?= server shared

.PHONY: check typecheck lint format fix server

check: typecheck lint format

typecheck:
	uv run python -m mypy server shared

lint:
	uv run ruff check server shared

format:
	uv run python -m black --check server shared

fix: 
	uv run ruff check --fix server shared
	uv run python -m black server shared

server:
	uv run python -m uvicorn server.src.main:app --reload
