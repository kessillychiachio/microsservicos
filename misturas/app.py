from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from contextlib import contextmanager
from database import Session
from models import Mistura, Oleo

app = FastAPI()

antagonicos = [
    ("Hortelã-pimenta", "Lavanda"),
    ("Alecrim", "Camomila"),
    ("Eucalipto", "Ylang Ylang")
]

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
        if db.query(Mistura).filter_by(nome=mistura.nome.strip().lower()).first():
            raise HTTPException(status_code=400, detail="Já existe uma mistura com esse nome.")

        for a1, a2 in antagonicos:
            if a1 in mistura.oleos and a2 in mistura.oleos:
                raise HTTPException(status_code=400, detail=f"Não é permitido combinar '{a1}' com '{a2}'.")

        nova = Mistura(nome=mistura.nome.strip().lower())
        db.add(nova)
        db.flush()

        for oleo in mistura.oleos:
            db.add(Oleo(nome=oleo, mistura_id=nova.id))

        db.commit()
        return {"mensagem": "Mistura salva com sucesso", "mistura": mistura}

@app.put("/misturas/{nome}")
def atualizar_mistura(nome: str, nova_mistura: MisturaSchema):
    with get_db() as db:
        mistura = db.query(Mistura).filter_by(nome=nome.strip().lower()).first()
        if not mistura:
            raise HTTPException(status_code=404, detail="Mistura não encontrada")

        for a1, a2 in antagonicos:
            if a1 in nova_mistura.oleos and a2 in nova_mistura.oleos:
                raise HTTPException(status_code=400, detail=f"Não é permitido combinar '{a1}' com '{a2}'.")

        db.query(Oleo).filter_by(mistura_id=mistura.id).delete()
        mistura.nome = nova_mistura.nome.strip().lower()
        for oleo in nova_mistura.oleos:
            db.add(Oleo(nome=oleo, mistura_id=mistura.id))

        db.commit()
        return {"mensagem": "Mistura atualizada com sucesso", "mistura": nova_mistura}

@app.delete("/misturas/{nome}")
def deletar_mistura(nome: str):
    with get_db() as db:
        mistura = db.query(Mistura).filter_by(nome=nome.strip().lower()).first()
        if not mistura:
            raise HTTPException(status_code=404, detail="Mistura não encontrada")
        db.delete(mistura)
        db.commit()
        return {"mensagem": "Mistura deletada com sucesso"}
