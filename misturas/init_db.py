from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from contextlib import contextmanager

from database import Session
from models import Mistura, Oleo, Antagonico

app = FastAPI()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class MisturaSchema(BaseModel):
    nome: str
    oleos: List[str]

def normalizar_oleos(oleos: List[str]) -> List[str]:
    return [oleo.strip().title() for oleo in oleos]

def validar_antagonicos(db, oleos: List[str]):
    oleos_set = set(normalizar_oleos(oleos))
    antagonicos = db.query(Antagonico).all()
    for ant in antagonicos:
        if {ant.oleo1, ant.oleo2}.issubset(oleos_set):
            raise HTTPException(
                status_code=400,
                detail=f"Não é permitido combinar '{ant.oleo1}' com '{ant.oleo2}'."
            )

@app.get("/misturas")
def listar_misturas():
    with get_db() as db:
        misturas = db.query(Mistura).all()
        return [
            {
                "nome": m.nome,
                "oleos": [o.nome for o in m.oleos]
            } for m in misturas
        ]

@app.post("/misturas")
def criar_mistura(mistura: MisturaSchema):
    with get_db() as db:
        nome_normalizado = mistura.nome.strip().lower()
        if db.query(Mistura).filter_by(nome=nome_normalizado).first():
            raise HTTPException(status_code=400, detail="Já existe uma mistura com esse nome.")

        validar_antagonicos(db, mistura.oleos)

        nova = Mistura(nome=nome_normalizado)
        db.add(nova)
        db.flush()

        for oleo_nome in normalizar_oleos(mistura.oleos):
            db.add(Oleo(nome=oleo_nome, mistura_id=nova.id))

        db.commit()
        return {"mensagem": "Mistura salva com sucesso", "mistura": mistura}

@app.put("/misturas/{nome}")
def atualizar_mistura(nome: str, nova_mistura: MisturaSchema):
    with get_db() as db:
        nome_normalizado = nome.strip().lower()
        mistura = db.query(Mistura).filter_by(nome=nome_normalizado).first()
        if not mistura:
            raise HTTPException(status_code=404, detail="Mistura não encontrada")

        validar_antagonicos(db, nova_mistura.oleos)

        db.query(Oleo).filter_by(mistura_id=mistura.id).delete()

        mistura.nome = nova_mistura.nome.strip().lower()
        for oleo_nome in normalizar_oleos(nova_mistura.oleos):
            db.add(Oleo(nome=oleo_nome, mistura_id=mistura.id))

        db.commit()
        return {"mensagem": "Mistura atualizada com sucesso", "mistura": nova_mistura}

@app.delete("/misturas/{nome}")
def deletar_mistura(nome: str):
    with get_db() as db:
        nome_normalizado = nome.strip().lower()
        mistura = db.query(Mistura).filter_by(nome=nome_normalizado).first()
        if not mistura:
            raise HTTPException(status_code=404, detail="Mistura não encontrada")

        db.delete(mistura)
        db.commit()
        return {"mensagem": "Mistura deletada com sucesso"}
