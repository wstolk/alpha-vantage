.PHONY: docs
init:
	pip install -e .[socks]
	pip install -r requirements-dev.txt
test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"