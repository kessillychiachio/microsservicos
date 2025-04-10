from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./oleos.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class oleoModel(Base):
    __tablename__ = "oleos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    beneficios = Column(String)
    
Base.metadata.create_all(bind=engine)



@app.get("/oleos")
def listar_oleos():
    return oleos

@app.post("/oleos")
def criar_oleo(oleo: dict):
    oleo["id"] = len(oleos) + 1
    oleos.append(oleo)
    return oleo

@app.put("/oleos/{oleo_id}")
def atualizar_oleo(oleo_id: int, dados: dict):
    for i, oleo in enumerate(oleos):
        if oleo["id"] == oleo_id:
            dados["id"] = oleo_id
            oleos[i] = dados
            return dados
    return {"erro": "Oleo nao encontrado"}

@app.delete("/oleos/{oleo_id}")
def deletar_oleo(oleo_id: int):
    for i, oleo in enumerate(oleos):
        if oleo["id"] == oleo_id:
            return oleos.pop(i)
    return {"erro": "Oleo nao encontrado"}

      
