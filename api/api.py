# api.py (FastAPI)
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Entrega(BaseModel):
    id: int
    cliente: str
    destino: str
    status: str
    
@app.post("/entregas/")

def criar_entrega(entrega: Entrega):
    conn = sqlite3.connect("entregas.db")
    conn.execute("INSERT INTO entregas VALUES (?, ?, ?, ?)", (entrega.id, entrega.cliente, entrega.destino, entrega.status))
    conn.commit()
    return {"mensagem": "Entrega criada com sucesso!"}