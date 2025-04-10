import requests

def tentar_requisicao(metodo, url, **kwargs):
  try:
    res = getattr(requests, metodo) (url, **kwargs)
    return res.json()
  except Exception as e:
    return f"Erro ao acessar {url}: {e}"
  
print("Catálogo de Óleos Essenciais:")
print(tentar_requisicao("get", "http://catalogo:5000/oleos"))

print("\nRecomendação por sintomas:")
print(tentar_requisicao("post", "http://recomendacoes:5000/recomendacoes"))

print("\n Criar mistura personalizada:")
mistura = {
  "nome": "Calmante e relaxante",
  "oleos": ["Lavanda", "Camomila", "Cedro"]
}
print(tentar_requisicao("post", "http://misturas:5000/misturas", json=mistura))

print("Misturas salvas:")
print(tentar_requisicao("get", "http://misturas:5000/misturas"))

print("Verificar contraindicações:")
perfil = {
  "perfil": ["gravidez", "epilepsia"],
  "oleos": ["Lavanda", "Alecrim", "Canela", "Hortelã-pimenta"]
}
print(tentar_requisicao("post", "http://contraindicacoes:5000/verificar", json=perfil))
