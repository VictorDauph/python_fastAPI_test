# README - FastAPI Scalping API (Full Docker)

## 🔎 Objectif

Application FastAPI dockerisée avec un environnement Conda pour déploiement, test et développement reproductible.

---

## 🐳 Lancer le projet avec Docker

### 1. Cloner le projet

```bash
git clone <repo-url>
cd python_fastAPI_test
```

### 2. Construire et lancer les conteneurs

```bash
docker-compose up --build
```

### 3. Accès à l'API

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠 Debug avec PyCharm

### Configuration

* Aller dans **Settings > Python Interpreter**
* Ajouter un interprète distant : `Docker Compose`

  * Service : `api`
  * Interpreter path : `/opt/conda/envs/fastapi_env/bin/python`

### Lancer en mode Debug

* Créer un Run Configuration (type: Python / module: uvicorn)
* Commande : `main:app --host 0.0.0.0 --port 8000 --reload`
* Working dir : racine du projet
* Env var : `PYTHONUNBUFFERED=1`
* Cocher emulate terminal in output console

### Attention :

* Si le `.env` n'est pas trouvé → spécifier le chemin manuellement dans la config
* Il peut y avoir des lenteurs en debug ≈ → lancer avec `docker-compose up` si besoin

---

## 🎓 Bonnes pratiques

* 🔍 Garde les `controllers` propres → pas de logique dans les routes
* 📄 `schemas_validators` = modèles Pydantic uniquement
* ✍️ Documente bien le setup pour pouvoir réinstaller sans douleur
* 🌐 Prépare un déploiement Render une fois l'API stable

---

## 🚀 Prochaines étapes

*

---

> Maintenu par Victor - Projet FastScalping - 2025
