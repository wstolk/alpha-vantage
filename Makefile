.PHONY: docs
init:
	pip install -e .[socks]
	pip install -r requirements-dev.txt
test:
	# This runs all of the tests, on both Python 2 and Python 3.
	detox

publish-test:
	pip3 install 'twine>=1.5.0'
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository testpypi dist/*
	rm -fr build dist .egg requests.egg-info

publish:
	pip3 install 'twine>=1.5.0'
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
	rm -fr build dist .egg alpha_vantage_py.egg-info

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"