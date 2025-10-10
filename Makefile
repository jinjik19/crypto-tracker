lint:
	pipenv run mypy src/ dags/

check-format:
	pipenv run ruff check

format:
	pipenv run ruff format