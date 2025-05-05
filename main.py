
import sys
print("Python utilisé :", sys.executable)


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue, petite flamme !!"}
