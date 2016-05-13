PYTHON=python3

all: README.md

README.md: README
	pandoc --from org --to markdown README > README.md

test: versiondiff
	echo "TEST 1"
	$(PYTHON) versiondiff tests/versions-4.3.3.cfg tests/versions-4.3.5.cfg
	echo "TEST 2"
	$(PYTHON) versiondiff tests/versions-4.3.5.cfg tests/versions-4.3.3.cfg
	echo "TEST 3"
	$(PYTHON) versiondiff tests/versions-4.3.5.cfg "https://dist.plone.org/release/4.2.1/versions.cfg"


.PHONY: test all
