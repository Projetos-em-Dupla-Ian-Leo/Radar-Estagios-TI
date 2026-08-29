from fastapi import FastAPI
import consultas
app = FastAPI()

@app.get("/vagas")
def vagas(area: str = None, prazo: str = None, sem_prazo: bool = False):
    resultado = consultas.listar_vagas(area = area, prazo = prazo, sem_prazo = sem_prazo)
    return resultado