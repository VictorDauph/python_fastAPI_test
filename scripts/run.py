import subprocess
import sys

def run_server():
    try:
        import fastapi  # simple vérification
        import uvicorn
    except ImportError:
        print("⚠️  Les dépendances ne sont pas installées dans l'environnement actuel.")
        print("➡️  Active d'abord ton environnement Conda :")
        print("    conda activate fastapi_env")
        print("➡️  Puis relance : python run.py")
        sys.exit(1)

    # Lance uvicorn
    subprocess.run(["uvicorn", "main:app", "--reload"])

if __name__ == "__main__":
    run_server()
