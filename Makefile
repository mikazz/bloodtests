PYTHON=     python3.7
VENV=       venv

$(VENV): $(VENV)/.depend


$(VENV)/.depend: requirements.txt
	# make venv
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install $(PIP_OPTIONS) -r requirements.txt


run: $(VENV)
	$(VENV)/bin/python manage.py runserver


test: $(VENV)
	$(VENV)/bin/pytest .


clean: $(VENV)
	Removing virtual environment
	rm -r $(VENV)


db:
	-rm -r bloodtests/migrations
	-rm -r db.sqlite3
	$(VENV)/bin/python manage.py makemigrations
	$(VENV)/bin/python manage.py makemigrations bloodtests
	$(VENV)/bin/python manage.py migrate bloodtests
	$(VENV)/bin/python manage.py loaddata 1.json
