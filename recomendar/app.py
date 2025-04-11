from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from contextlib import contextmanager
from database import Session
from models import Sugestao

app = FastAPI()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class Sintomas(BaseModel):
    sintomas: List[str]

@app.get("/recomendar")
def listar_sugestoes():
    with get_db() as db:
        sugestoes = db.query(Sugestao).all()
        agrupadas = {}
        for s in sugestoes:
            agrupadas.setdefault(s.sintoma, []).append(s.oleo)
        return agrupadas

@app.post("/recomendar")
def recomendar(sintomas: Sintomas):
    resultado = set()
    with get_db() as db:
        for sintoma in sintomas.sintomas:
            oleos = db.query(Sugestao).filter_by(sintoma=sintoma.strip().lower()).all()
            resultado.update([s.oleo for s in oleos])
    return {"recomendados": list(resultado)}

@app.put("/recomendar/{sintoma}")
def atualizar_sugestoes(sintoma: str, novos_oleos: List[str]):
    with get_db() as db:
        sintoma = sintoma.strip().lower()
        registros = db.query(Sugestao).filter_by(sintoma=sintoma).all()
        if not registros:
            raise HTTPException(status_code=404, detail="Sintoma não encontrado")

        db.query(Sugestao).filter_by(sintoma=sintoma).delete()
        for oleo in novos_oleos:
            db.add(Sugestao(sintoma=sintoma, oleo=oleo))
        db.commit()
        return {"mensagem": f"Óleos para '{sintoma}' atualizados com sucesso."}

@app.delete("/recomendar/{sintoma}")
def deletar_sugestao(sintoma: str):
    with get_db() as db:
        sintoma = sintoma.strip().lower()
        registros = db.query(Sugestao).filter_by(sintoma=sintoma).all()
        if not registros:
            raise HTTPException(status_code=404, detail="Sintoma não encontrado")
        db.query(Sugestao).filter_by(sintoma=sintoma).delete()
        db.commit()
        return {"mensagem": f"Sugestões para '{sintoma}' removidas com sucesso."}
