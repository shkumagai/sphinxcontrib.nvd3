.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' \
	| sort

-include env.mk

.PHONY: package
package: ## build packages
	uv build

.PHONE: release-test
release-test: ## release packages to testpypi
	uv build
	UV_PUBLISH_TOKEN=$$(op read $(TESTPYPI_TOKEN_REF)) uv publish --publish-url https://test.pypi.org/legacy/

.PHONY: release-prod
release-prod: ## release packages to pypi
	uv build
	UV_PUBLISH_TOKEN=$$(op read $(PYPI_TOKEN_REF)) uv publish

.PHONY: clear-dist
clear-dist: ## clear package files
	@-rm -rf dist/*

.PHONY: test
test: ## run tests
	tox
