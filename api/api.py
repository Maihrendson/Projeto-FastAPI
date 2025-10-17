# api.py (FastAPI)
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI() #Cria a instância do FastAPI.

class Entrega(BaseModel): #Classe para definir o modelo de dados.
    id: int
    cliente: str
    destino: str
    status: str
    
@app.post("/entregas/") #Cria uma rota para criar uma nova entrega.

def criar_entrega(entrega: Entrega): #Função de criar uma nova entrega.
    conn = sqlite3.connect("entregas.db")
    conn.execute("INSERT INTO entregas VALUES (?, ?, ?, ?)", (entrega.id, entrega.cliente, entrega.destino, entrega.status))
    conn.commit()
    return {"mensagem": "Entrega criada com sucesso!"}

@app.get("/entregas/") #Cria uma instância para listar todas as entregas.

def listar_entregas(): #Cria uma função para listar todas as entregas.
    conn = sqlite3.connect("entregas.db")
    cursor = conn.execute("SELECT * FROM entregas")
    entregas = cursor.fetchall()
    return {"entregas": entregas}