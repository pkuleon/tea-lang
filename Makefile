init:
	pip install pipenv
	pipenv install --dev

test:
	# pipenv run pytest ./tests/integration_tests/test_integration.py # Commented out for the time being while rewriting API
	pipenv run pytest ./tests/unit_tests/test_new_api.py