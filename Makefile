install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

