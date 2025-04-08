from fastapi import FastAPI, Body

app = FastAPI()

sugestoes = {
  "ansiedade": ["Lavanda", "Camomila", "Bergamota"],
  "insônia": ["Lavanda", "Manjerona", "Cedro"],
  "estresse": ["Hortelã-pimenta", "Ylang Ylang", "Laranja-selvagem"]
}

@app.post("/recomendar"):
def recomendar(sintomas: list[str] = Body(...)):
    resultado = set()
    for sintoma in sintomas:
      resultado.update(sugestoes.get(sintoma.lower(), []))
    return {"recomendados": list(resultado)}