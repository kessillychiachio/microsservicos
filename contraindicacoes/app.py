from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database import Session
from models import Perfil, OleoContraindicado
from contextlib import contextmanager

app = FastAPI()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class ConsultaContraIndicacao(BaseModel):
    perfil: List[str]
    oleos: List[str]

class AtualizacaoPerfil(BaseModel):
    oleos: List[str]

@app.get("/contraindicacoes")
def listar_contraindicacoes():
    with get_db() as db:
        perfis = db.query(Perfil).all()
        return {p.nome: [o.oleo for o in p.oleos] for p in perfis}

@app.post("/contraindicacoes")
def verificar_contraindicacoes(consulta: ConsultaContraIndicacao):
    perigosos = set()
    with get_db() as db:
        for nome_perfil in consulta.perfil:
            perfil = db.query(Perfil).filter_by(nome=nome_perfil.strip().lower()).first()
            if perfil:
                contra = [o.oleo.strip().lower() for o in perfil.oleos]
                for oleo in consulta.oleos:
                    if oleo.lower() in contra:
                        perigosos.add(oleo)
    return {"contraindicados": list(perigosos)}

@app.put("/contraindicacoes/{perfil}")
def atualizar_perfil(perfil: str, dados: AtualizacaoPerfil):
    with get_db() as db:
        p = db.query(Perfil).filter_by(nome=perfil.strip().lower()).first()
        if not p:
            p = Perfil(nome=perfil.strip().lower())
            db.add(p)
            db.flush()
        db.query(OleoContraindicado).filter_by(perfil_id=p.id).delete()
        for oleo in dados.oleos:
            db.add(OleoContraindicado(oleo=oleo, perfil_id=p.id))
        db.commit()
        return {perfil: dados.oleos}

@app.delete("/contraindicacoes/{perfil}")
def remover_perfil(perfil: str):
    with get_db() as db:
        p = db.query(Perfil).filter_by(nome=perfil.strip().lower()).first()
        if not p:
            raise HTTPException(status_code=404, detail="Perfil não encontrado.")
        db.delete(p)
        db.commit()
        return {"removido": perfil}
