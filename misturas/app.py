from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

misturas_salvas = []

antagonicos = [
  ("Hortelã-pimenta", "Lavanda"),
  ("Alecrim", "Camomila"),
  ("Eucalipto", "Ylang Ylang")
]

class Mistura (BaseModel):
 nome: str
 oleos: list[str]
 
@app.post("/misturas")
def criar_mistura(mistura: Mistura):
    for a1, a2 in antagonicos:
        if a1 in mistura.oleos and a2 in mistura.oleos:
            raise HTTPException(
                status_code=400,
                detail=f"Não é permitido combinar '{a1}' com '{a2}' na mesma mistura, pois os seus efeitos são inversos e não agregam juntos. Escolha outros óleos."
            )
    misturas_salvas.append(mistura)
    return {"mensagem": "Mistura salva com sucesso", "mistura": mistura}

@app.get("/misturas")
def listar_misturas():
  return misturas_salvas