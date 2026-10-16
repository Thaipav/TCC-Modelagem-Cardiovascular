from fastapi import FastAPI

cardio_api = FastAPI()

@cardio_api.get("/")
def home():
    return {"status": "Ambiente rodando com sucesso!"} 