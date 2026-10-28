SRC ?= src/server src/model

# Sounds play in the background so they never slow the command down
PLAY = sh ../.githooks/play
SOUND = $(PLAY) $(1) >/dev/null 2>&1 &

.PHONY: check typecheck lint format fix server

check: typecheck lint format
	@$(call SOUND,success)

typecheck:
	@uv run python -m mypy $(SRC) || { $(call SOUND,no) exit 1; }

lint:
	@$(call SOUND,ruff)
	@uv run ruff check $(SRC) || { $(call SOUND,fail) exit 1; }

format:
	@$(call SOUND,black)
	@uv run python -m black --check $(SRC) || { $(call SOUND,fail) exit 1; }

fix:
	@$(call SOUND,ruff)
	uv run ruff check --fix $(SRC)
	@$(call SOUND,black)
	uv run python -m black $(SRC)

server:
	@$(call SOUND,build)
	uv run python -m uvicorn server.main:app --reload
