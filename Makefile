.PHONY: package release-test release-prod clear-dist test isort black flake8

package:
	poetry build

release-test:
	poetry public -r testpypi --build

release-prod:
	poetry public -r test --build

clear-dist:
	-rm -rf dist/*

test:
	tox
