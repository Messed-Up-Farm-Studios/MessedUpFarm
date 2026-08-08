.PHONY: check typecheck lint format server

check: typecheck lint format

typecheck:
	uv run python -m mypy server

lint:
	uv run python -m mypy server

format:
	uv run python -m black --check server

server:
	uv run python -m uvicorn server.app.server:app --reload
