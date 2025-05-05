# Projet FastAPI - Environnement Conda

## lancer le projet quand installé!
````bash
# 1. Active l'environnement Conda
conda activate fastapi_env

# 2. Lance le serveur
uvicorn main:app --reload

````
Ce projet utilise un environnement Conda pour garantir un environnement reproductible.
Il sera dockerisé à terme.

## 🔁 Recréer l’environnement

Pour installer toutes les dépendances et configurer un environnement identique :

```bash
conda env create -f environment.yml
conda activate fastapi_env
```

## Exporter l’environnement à jour
Si tu ajoutes de nouvelles dépendances avec conda install, pense à mettre à jour le fichier environment.yml :

```bash
conda activate fastapi_env
conda env export --from-history > environment.yml
```

💡 Le flag --from-history permet de ne conserver que les paquets explicitement installés, pour un fichier plus propre et portable.

## ✅ Bonnes pratiques
N’utilise pas pip install dans cet environnement (sauf si absolument nécessaire)

Pour ajouter un nouveau paquet :

```bash

conda install nom_du_paquet
conda env export --from-history > environment.yml
```
Ne versionne jamais le dossier .conda ou .venv