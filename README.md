# Health Calculator Microservice

## **Prérequis**

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

1. **Python 3.12 ou plus récent**
   - Vous pouvez vérifier votre version avec :
     ```bash
     python3 --version
     ```

2. **Pip** (gestionnaire de paquets Python)
   - Assurez-vous que pip est installé :
     ```bash
     pip --version
     ```

3. **Docker** (pour la containerisation)
   - Vérifiez que Docker est installé :
     ```bash
     docker --version
     ```

4. **Git** (pour cloner le répertoire)
   - Assurez-vous que Git est installé :
     ```bash
     git --version
     ```

## **Installation et exécution locale**

### 1. **Cloner le dépôt Git**
Cloner le dépôt sur votre machine locale :
```bash
git clone https://github.com/sseey/Health-Calculator.git
cd Health-Calculator
```

### 2. **Créer un environnement virtuel**
Créez un environnement Python isolé :
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/MacOS
venv\Scripts\activate    # Sur Windows
```

### 3. **Installer les dépendances**
Installez les dépendances requises depuis `requirements.txt` :
```bash
pip install -r requirements.txt
```

### 4. **Lancer l'application Flask**
Démarrez le serveur Flask localement :
```bash
python app.py
```

L'application sera disponible à l'adresse : [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Tester l'application**

### 1. **Tests unitaires**
Tous les tests unitaires sont regroupés dans le répertoire `tests/`.

#### Lancer les tests unitaires :
Depuis la racine du projet, exécutez :
```bash
python -m unittest discover -s tests
```

#### Détails des tests :
- **`tests/test_health_utils.py`** : Tests unitaires pour les fonctions de calcul du BMI et BMR.
- **`tests/test_app.py`** : Tests des endpoints de l'API Flask.

### 2. **Tester via le navigateur**
Accédez à [http://127.0.0.1:5000](http://127.0.0.1:5000) pour utiliser l'interface utilisateur simplifiée avec des formulaires HTML.

### 3. **Tester via Docker**

#### Construire l'image Docker :
Depuis la racine du projet :
```bash
docker build -t health-calculator .
```

#### Lancer le conteneur :
```bash
docker run -p 5000:5000 health-calculator
```

Accédez à [http://127.0.0.1:5000](http://127.0.0.1:5000) pour utiliser l'application dans un environnement Docker.

---

## **Technologies utilisées**

1. **Python 3.12** :
   - Langage principal pour la logique des calculs et l'implémentation de l'API.

2. **Flask** :
   - Framework léger pour créer l'API REST et servir une interface utilisateur HTML simple.

3. **Unittest** :
   - Framework de test pour valider les calculs (BMI, BMR) et les endpoints de l'API.

4. **Docker** :
   - Pour containeriser l'application et simplifier son déploiement.

---

## **Détails des fichiers du projet**

1. **`app.py`** :
   - Contient le code principal de l'API Flask avec les endpoints suivants :
     - `/bmi` : Calcule le BMI (Body Mass Index).
     - `/bmr` : Calcule le BMR (Basal Metabolic Rate).

2. **`health_utils.py`** :
   - Contient les fonctions utilitaires suivantes :
     - `calculate_bmi(height, weight)` : Calcule le BMI à partir de la taille et du poids.
     - `calculate_bmr(height, weight, age, gender)` : Calcule le BMR à partir de la taille, du poids, de l'âge et du genre.

3. **`tests/test_health_utils.py`** :
   - Tests unitaires des fonctions utilitaires (`calculate_bmi`, `calculate_bmr`).

4. **`tests/test_app.py`** :
   - Tests des endpoints Flask (`/bmi`, `/bmr`).

5. **`Dockerfile`** :
   - Instructions pour containeriser l'application.

6. **`requirements.txt`** :
   - Liste des dépendances Python requises pour exécuter l'application.

---

## **Justification pour les tests séparés**

Les tests sont organisés dans deux fichiers distincts pour améliorer la lisibilité et faciliter la maintenance :

1. **`test_health_utils.py`** :
   - Se concentre uniquement sur les fonctions utilitaires de calcul.
   - Garantit que la logique mathématique est correcte et isolée de l'API.

2. **`test_app.py`** :
   - Se concentre sur l'API Flask.
   - Valide que les endpoints fonctionnent correctement avec des requêtes HTTP (cas valides et invalides).

**Avantages de cette approche :**
- Favorise une responsabilité unique par fichier.
- Facilite le débogage en cas d'échec d'un test.
- Rend le projet plus modulaire et maintenable.

---

## **Sources**

- https://www.sololearn.com/en/discuss/2686226/bmi-calculator-python-beginner-project
- https://docs.python.org/3/library/unittest.html
- https://hub.docker.com/_/python
- 