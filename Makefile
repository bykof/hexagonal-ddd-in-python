.PHONY: lint lint-fix format


lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

format:
	uv run ruff format

test:
	uv run pytest .