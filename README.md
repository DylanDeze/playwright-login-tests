# Playwright Login Tests

## Description
Ce projet utilise **Playwright** pour automatiser et tester le formulaire de connexion du site :
[Practice Test Automation](https://practicetestautomation.com/practice-test-login/)

Les tests vérifient :
- Le succès d'une connexion avec de bonnes informations
- Les erreurs de connexion avec un mauvais identifiant
- Les erreurs de connexion avec un mauvais mot de passe

---

## Structure du projet
Voici la structure des fichiers et répertoires de ce projet :

- /screenshots/ → Captures d'écran prises en cas d'échec
- /tests/test_login.py → Script principal des tests 
- README.md → Ce fichier


---

## Prérequis
- Python 3.9+
- Playwright
- Environnement virtuel recommandé

---

## Installation
1. Créer et activer un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

2. Installer Playwright :

```bash
pip install playwright
```

3. Installer les navigateurs nécessaires :

```bash
playwright install
```
## Exécution des tests

Lancer directement dans ton terminal (dans le dossier du projet) :

```bash
python test_login.py
```
Cela exécutera tous les tests et ouvrira un navigateur Chromium pour vérifier la connexion. Si un test échoue, une capture d'écran sera enregistrée dans le dossier **/screenshots/**.

## Exemple de sortie console attendue

```bash
✅ test_login_success passed
❌ test_login_invalid_username failed: AssertionError: Error message for invalid username not visible
✅ test_login_invalid_password passed

```

## Auteur 

- Dylan
