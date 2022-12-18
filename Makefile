install:
	poetry install
	poetry build

reinstall:
	pip install --user --force-reinstall dist/*.whl
