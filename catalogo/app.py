from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "sqlite:///./catalogo.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()

class OleoModel(Base):
    __tablename__ = "oleos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    beneficios = Column(String)

Base.metadata.create_all(bind=engine)

class Oleo(BaseModel):
    nome: str
    beneficios: List[str]

@app.get("/oleos")
def listar_oleos():
    db = Session()
    oleos = db.query(OleoModel).all()
    return [{"id": o.id, "nome": o.nome, "beneficios": o.beneficios.split(";")} for o in oleos]

@app.post("/oleos")
def criar_oleo(oleo: Oleo):
    db = Session()
    existe = db.query(OleoModel).filter_by(nome=oleo.nome).first()
    if existe:
        raise HTTPException(status_code=400, detail="Óleo já existe.")
    novo = OleoModel(nome=oleo.nome, beneficios=";".join(oleo.beneficios))
    db.add(novo)
    db.commit()
    return {"mensagem": "Óleo adicionado com sucesso"}

@app.put("/oleos/{oleo_id}")
def atualizar_oleo(oleo_id: int, oleo: Oleo):
    db = Session()
    item = db.query(OleoModel).filter_by(id=oleo_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Óleo não encontrado.")
    item.nome = oleo.nome
    item.beneficios = ";".join(oleo.beneficios)
    db.commit()
    return {"mensagem": "Óleo atualizado com sucesso"}

@app.delete("/oleos/{oleo_id}")
def deletar_oleo(oleo_id: int):
    db = Session()
    item = db.query(OleoModel).filter_by(id=oleo_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Óleo não encontrado.")
    db.delete(item)
    db.commit()
    return {"mensagem": "Óleo removido com sucesso"}
