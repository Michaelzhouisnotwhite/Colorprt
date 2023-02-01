install:
	python -m setup.py install

b:
	python -m build


dir:="dist/*"
upload:
	python -m twine	upload ${dir}