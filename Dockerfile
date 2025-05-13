FROM continuumio/miniconda3

# Définir le dossier de travail
WORKDIR /app

# Copier l’environnement
COPY environment.yml .

# Créer l'environnement conda
RUN conda env create -f environment.yml

# Activer l’environnement
SHELL ["conda", "run", "-n", "fastapi_env", "/bin/bash", "-c"]

# Copier le reste du projet
COPY . .

# Exposer le port de l'API
EXPOSE 8000

# Lancer l’API dans l’environnement conda
CMD ["conda", "run", "-n", "fastapi_env", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

