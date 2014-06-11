.PHONY: pypi

pypi:
	python setup.py build sdist register upload
