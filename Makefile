lint:
	poetry run black --check .
	poetry run isort -c .
	poetry run flake8 .
format:
	poetry run black .
	poetry run isort .
	poetry run autoflake --in-place --remove-all-unused-imports -r .
test:
	poetry run pytest
