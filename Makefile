.PHONY: build

build:
	python3 setup.py bdist_wheel

upload:
	twine upload dist/*
