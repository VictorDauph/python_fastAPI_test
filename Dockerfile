FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

# Créer l'environnement conda
RUN conda env create -f environment.yml

# Étendre le PATH pour accéder à l'env conda
ENV PATH /opt/conda/envs/fastapi_env/bin:$PATH

COPY . .

EXPOSE 8000 5678

# ✅ Lancer uvicorn sans conda run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
