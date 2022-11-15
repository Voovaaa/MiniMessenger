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

makemigrations:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

shell:
	poetry run ./manage.py shell