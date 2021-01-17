install:
	# install mipypro
	python setup.py install

test.unit:
	# test units of mipypro
	python -m pytest -m "not integration"

test.integration:
	# test end-to-end function
	rm -rf orthofisher_output/
	python -m pytest --basetemp=output -m "integration"

test:
	## execute both integration and unit tests
	# unit tests
	python -m pytest -m "not integration"
	# integration tests
	python -m pytest --basetemp=output -m "integration"

# used by GitHub actions during CI workflow
test.coverage: coverage.unit coverage.integration

coverage.unit:
	python -m pytest --cov=./ -m "not integration" --cov-report=xml:unit.coverage.xml

coverage.integration:
	rm -rf output/
	mkdir output/
	python -m pytest --basetemp=output --cov=./ -m "integration" --cov-report=xml:integration.coverage.xml