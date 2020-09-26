setup:
	python3 -m venv ~/.cirepo

activate:
	source ~/.cirepo/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=cirepolib tests/*.py
	python -m pytest --nbval notebook.ipynb

lint:
	pylint --disable=R,C cirepolib cli tests/test_cirepo

all: install lint test

