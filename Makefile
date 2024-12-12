# Variables
VENV = venv
PYTHON = python3
PIP = $(VENV)/bin/pip
ACTIVATE = source $(VENV)/bin/activate

# Créer un environnement virtuel
venv: 
	$(PYTHON) -m venv $(VENV)
	@echo "Environnement virtuel créé. Activez-le avec 'source $(VENV)/bin/activate'"

# Installer les dépendances
install: venv
	$(PIP) install -r requirements.txt
	@echo "Dépendances installées."

# Lancer le serveur Flask
run: install
	. $(VENV)/bin/activate && python app.py

# Lancer les tests unitaires
test: install
	. $(VENV)/bin/activate && python -m unittest discover -s tests

# Nettoyer le projet
clean:
	rm -rf $(VENV) __pycache__ */__pycache__
	@echo "Environnement virtuel et caches Python supprimés."
