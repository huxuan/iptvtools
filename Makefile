.PHONY: clean deps install lint pycodestyle pyflakes pylint dist upload

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf build dist *.egg-info .eggs *.spec

deps:
	pip install -r requirements.txt

install:
	python setup.py install

lint: pycodestyle pyflakes pylint

pycodestyle:
	-pycodestyle setup.py iptvtools

pyflakes:
	-pyflakes setup.py iptvtools

pylint:
	-pylint setup.py iptvtools

dist:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

test:
	python -m iptvtools.iptv_filter -i test.in.m3u -t test.m3u -u http://192.168.50.1:8888 -o test.out.m3u

test1:
	iptv-filter -i test.in.m3u -t test.m3u -u http://192.168.50.1:8888 -o test1.out.m3u

test2:
	python -m iptvtools.iptv_filter -i bj-unicom-iptv.m3u -t test.m3u -u http://192.168.50.1:8888 -o test2.out.m3u
