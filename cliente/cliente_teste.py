import requests

def tentar_requisicao(metodo, url, **kwargs):
    try:
        res = getattr(requests, metodo)(url, **kwargs)
        return res.json()
    except Exception as e:
        return f"Erro ao acessar {url}: {e}"

print("\n[1] Catálogo de Óleos Essenciais:")
print(tentar_requisicao("get", "http://catalogo:5000/oleos"))

print("\n[2] Recomendação por sintomas:")
sintomas = ["ansiedade", "insônia"]
print(tentar_requisicao("post", "http://recomendar:5000/recomendar", json=sintomas))

print("\n[3] Criar mistura personalizada:")
mistura = {
    "nome": "Calmante Noturno",
    "oleos": ["Lavanda", "Camomila", "Cedro"]
}
print(tentar_requisicao("post", "http://misturas:5000/misturas", json=mistura))

print("\n[4] Misturas salvas:")
print(tentar_requisicao("get", "http://misturas:5000/misturas"))

print("\n[5] Verificar contraindicações:")
perfil = {
    "perfil": ["gravidez", "epilepsia"],
    "oleos": ["Lavanda", "Alecrim", "Canela", "Hortelã-pimenta"]
}
print(tentar_requisicao("post", "http://contraindicacoes:5000/verificar", json=perfil))
