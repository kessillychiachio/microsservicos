from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

contraindicacoes = [
  "gravidez": ["Alecrim", "Canela", "Cravo", "Salvia", "Manjerona", "Gengibre"],
  "epilepsia": ["Alecrim", "Eucalipto", "Hortelã-pimenta"],
  "pressao alta": ["Alecrim", "Tomilho", "Hortelã-pimenta"],
  "pressao baixa": ["Ylang Ylang", "Camomila"]
]

class ConsultaContraIndicacao(BaseModel):
  perfil: List[str]
  oleos: List[str]
  
  
@app.post ("/verificar")
def verificar_contraindicacoes(consulta: ConsultaContraIndicacao):
    perigosos = set()
    
    for grupo in consulta.perfil:
      lista = contraindicacoes.get(grupo.lower(), [])
      for oleo in consulta.oleos:
        if oleo in list:
          perigosos.add(oleo)
          
    return {"contraindicados": list(perigosos)}