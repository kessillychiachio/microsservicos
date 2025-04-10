from fastapi import FastAPI

app = FastAPI()

oleos = [
  {"id": 1, "nome": "Lavanda", "beneficios": ["calmante", "relaxante", "auxilia no sono"]},
  {"id": 2, "nome": "Hortelã-pimenta", "beneficios": ["revigorante", "alivia dores de cabeça", "descongestionante"]},
  {"id": 3, "nome": "Tea Tree", "beneficios": ["antisséptico", "antifúngico", "cicatrizante"]}
]

@app.get("/oleos")
def listar_oleos():
  return oleos

@app.get("/oleos/{oleo_id}")
def detalhar_oleo(oleo_id: int):
  for oleo in oleos:
    if oleo["id"] == oleo_id:
      return oleo
  return {"erro": "Oleo nao encontrado"}
