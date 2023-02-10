install:
	pip install -e .

b:
	python -m build


dir:="dist/*"
upload:
	python -m twine	upload ${dir}