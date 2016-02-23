install-dev:
	python setup.py develop --user
install-local:
	python setup.py install --user
install:
	python setup.py install
test:
	python setup.py test
doc-html:
	make -C doc/ html
	#nojekyll for gh-pages
	touch doc/build/html/.nojekyll
update-gh-pages:
	@echo "Warning: Black magic in action"
	git push origin `git subtree split --prefix doc/build/html/ master`:gh-pages --force
init-sphinx:
	sphinx-quickstart --no-batchfile --project "abitiny" --author "Alejandro Gallo" --makefile --ext-autodoc

.PHONY: deps

all: deps
	PYTHONPATH=.venv ; . .venv/bin/activate

.venv:
	if [ ! -e ".venv/bin/activate_this.py" ] ; then virtualenv --clear .venv ; fi

deps: .venv requirements.txt
	PYTHONPATH=.venv ; . .venv/bin/activate && .venv/bin/pip install -U -r requirements.txt

clean:
	rm -rf .venv build *.egg-info
	rm -f `find . -name \*.pyc -print0 | xargs -0`
