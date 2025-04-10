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

class Mistura(BaseModel):
    nome: str
    oleos: List[str]

@app.get("/misturas")
def listar_misturas():
    return misturas_salvas

@app.post("/misturas")
def criar_mistura(mistura: Mistura):
    for m in misturas_salvas:
        if m.nome.lower() == mistura.nome.lower():
            raise HTTPException(
                status_code=400,
                detail=f"Já existe uma mistura com o nome '{mistura.nome}'."
            )

    for a1, a2 in antagonicos:
        if a1 in mistura.oleos and a2 in mistura.oleos:
            raise HTTPException(
                status_code=400,
                detail=f"Não é permitido combinar '{a1}' com '{a2}' na mesma mistura."
            )

    misturas_salvas.append(mistura)
    return {"mensagem": "Mistura salva com sucesso", "mistura": mistura}

@app.put("/misturas/{nome}")
def atualizar_mistura(nome: str, nova_mistura: Mistura):
    for i, m in enumerate(misturas_salvas):
        if m.nome.lower() == nome.lower():
            for a1, a2 in antagonicos:
                if a1 in nova_mistura.oleos and a2 in nova_mistura.oleos:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Não é permitido combinar '{a1}' com '{a2}' na mesma mistura."
                    )
            misturas_salvas[i] = nova_mistura
            return {"mensagem": "Mistura atualizada com sucesso", "mistura": nova_mistura}
    raise HTTPException(status_code=404, detail="Mistura não encontrada")

@app.delete("/misturas/{nome}")
def deletar_mistura(nome: str):
    for mistura in misturas_salvas:
        if mistura.nome.lower() == nome.lower():
            misturas_salvas.remove(mistura)
            return {"mensagem": "Mistura deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Mistura não encontrada")
