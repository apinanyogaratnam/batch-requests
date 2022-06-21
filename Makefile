.PHONY: build

build:
	python3 setup.py bdist_wheel

upload:
	twine upload dist/*

lint:
	autopep8 autopep8 --in-place --aggressive --aggressive batch.py --max-line-length 120
