from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

sugestoes = {
    "ansiedade": ["Lavanda", "Camomila", "Bergamota"],
    "insônia": ["Lavanda", "Manjerona", "Cedro"],
    "estresse": ["Hortelã-pimenta", "Ylang Ylang", "Laranja-selvagem"]
}

class Sintomas(BaseModel):
    sintomas: List[str]

@app.get("/recomendar")
def listar_sugestoes():
    return sugestoes

@app.post("/recomendar")
def recomendar(sintomas: Sintomas):
    resultado = set()
    for sintoma in sintomas.sintomas:
        resultado.update(sugestoes.get(sintoma.lower(), []))
    return {"recomendados": list(resultado)}

@app.put("/recomendar/{sintoma}")
def atualizar_sugestoes(sintoma: str, novos_oleos: List[str]):
    if sintoma.lower() in sugestoes:
        sugestoes[sintoma.lower()] = novos_oleos
        return {"mensagem": f"Óleos para '{sintoma}' atualizados com sucesso."}
    raise HTTPException(status_code=404, detail="Sintoma não encontrado")

@app.delete("/recomendar/{sintoma}")
def deletar_sugestao(sintoma: str):
    if sintoma.lower() in sugestoes:
        del sugestoes[sintoma.lower()]
        return {"mensagem": f"Sugestões para '{sintoma}' removidas com sucesso."}
    raise HTTPException(status_code=404, detail="Sintoma não encontrado")
