from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

app = FastAPI()

DATABASE_URL = "sqlite:///./catalogo.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        
class OleoModel(Base):
    __tablename__ = "oleos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    beneficios = Column(String)

Base.metadata.create_all(bind=engine)

class Oleo(BaseModel):
    nome: str
    beneficios: List[str]

class OleoResponse(Oleo):
    id: int

    class Config:
        orm_mode = True

@app.get("/oleos", response_model=List[OleoResponse])
def listar_oleos():
    with get_db() as db:
        oleos = db.query(OleoModel).all()
        return [
            OleoResponse(
                id=oleo.id,
                nome=oleo.nome,
                beneficios=oleo.beneficios.split(";")
                for oleo in oleos
            )
        ]
@app.post("/oleos", response_model=dict)
def criar_oleo(oleo: Oleo):
    with get_db() as db:
        existe = db.query(OleoModel).filter_by(nome=oleo.nome).first()
        if existe:
            raise HTTPException(status_code=400, detail="Oleo já existe")
        novo = OleoModel(nome=oleo.nome, beneficios=";".join(oleo.beneficios))
        db.add(novo)
        db.commit()
        return {"message": "Oleo criado com sucesso"}

@app.put("/oleos/{oleo_id}", response_model=dict)
def atualizar_oleo(oleo_id: int, oleo: Oleo):
    with get_db() as db:
        item = db.query(OleoModel).filter_by(id=oleo_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Oleo não encontrado")
        item.nome = oleo.nome
        item.beneficios = ";".join(oleo.beneficios)
        db.commit()
        return {"message": "Oleo atualizado com sucesso"}
    
@app.delete("/oleos/{oleo_id}", response_model=dict)
def deletar_oleo(oleo_id: int):
    with get_db() as db:
        item = db.query(OleoModel).filter_by(id=oleo_id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Oleo não encontrado")
        db.delete(item)
        db.commit()
        return {"message": "Oleo deletado com sucesso"}
