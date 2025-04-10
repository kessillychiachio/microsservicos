from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

contraindicacoes = {
    "gravidez": ["Alecrim", "Canela", "Cravo", "Salvia", "Manjerona", "Gengibre"],
    "epilepsia": ["Alecrim", "Eucalipto", "Hortelã-pimenta"],
    "pressao alta": ["Alecrim", "Tomilho", "Hortelã-pimenta"],
    "pressao baixa": ["Ylang Ylang", "Camomila"]
}

class ConsultaContraIndicacao(BaseModel):
    perfil: List[str]
    oleos: List[str]

class AtualizacaoPerfil(BaseModel):
    oleos: List[str]

@app.get("/contraindicacoes")
def listar_contraindicacoes():
    return contraindicacoes

@app.post("/contraindicacoes")
def verificar_contraindicacoes(consulta: ConsultaContraIndicacao):
    perigosos = set()
    for grupo in consulta.perfil:
        lista = contraindicacoes.get(grupo.lower(), [])
        for oleo in consulta.oleos:
            if oleo in lista:
                perigosos.add(oleo)
    return {"contraindicados": list(perigosos)}

@app.put("/contraindicacoes/{perfil}")
def atualizar_perfil(perfil: str, dados: AtualizacaoPerfil):
    contraindicacoes[perfil.lower()] = dados.oleos
    return {perfil: dados.oleos}

@app.delete("/contraindicacoes/{perfil}")
def remover_perfil(perfil: str):
    removido = contraindicacoes.pop(perfil.lower(), None)
    if removido is None:
        return {"erro": "Perfil não encontrado"}
    return {"removido": perfil, "oleos": removido}
