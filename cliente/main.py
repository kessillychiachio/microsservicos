import requests
import time

def tentar_requisicao(metodo, url, tentativas=3, **kwargs):
    for tentativa in range(tentativas):
        try:
            res = getattr(requests, metodo)(url, **kwargs)
            return True, res.json()
        except Exception as e:
            print(f"Tentativa {tentativa + 1} falhou para {url}: {e}")
            time.sleep(2)
    return False, None

def executar_cliente():
    while True:
        print("\n--- CONSULTA DE ÓLEOS ESSENCIAIS ---")

        sucesso, dados = tentar_requisicao("get", "http://catalogo:8000/oleos")
        print("Catálogo:", dados if sucesso else "Indisponível.")

        sintomas = {"sintomas": ["ansiedade", "insônia"]}
        sucesso, dados = tentar_requisicao("post", "http://recomendar:8000/recomendar", json=sintomas)
        print("Recomendações:", dados if sucesso else "Indisponível.")

        nova_lista = ["Lavanda", "Bergamota", "Vetiver"]
        sucesso, dados = tentar_requisicao("put", "http://recomendar:8000/recomendar/ansiedade", json=nova_lista)
        print("Atualização de sugestão:", dados if sucesso else "Falha.")

        sucesso, dados = tentar_requisicao("delete", "http://recomendar:8000/recomendar/insônia")
        print("Exclusão de sugestão:", dados if sucesso else "Falha.")

        mistura = {
            "nome": "Relax Mix",
            "oleos": ["Lavanda", "Camomila", "Cedro"]
        }
        sucesso, dados = tentar_requisicao("post", "http://misturas:8000/misturas", json=mistura)
        print("Mistura criada:", dados if sucesso else "Falha.")

        nova_mistura = {
            "nome": "Relax Mix",
            "oleos": ["Lavanda", "Camomila"]
        }
        sucesso, dados = tentar_requisicao("put", "http://misturas:8000/misturas/Relax Mix", json=nova_mistura)
        print("Mistura atualizada:", dados if sucesso else "Falha.")

        sucesso, dados = tentar_requisicao("get", "http://misturas:8000/misturas")
        print("Misturas salvas:", dados if sucesso else "Indisponível.")

        sucesso, dados = tentar_requisicao("delete", "http://misturas:8000/misturas/Relax Mix")
        print("Mistura deletada:", dados if sucesso else "Falha.")

        perfil = {
            "perfil": ["gravidez", "epilepsia"],
            "oleos": ["Lavanda", "Alecrim", "Canela", "Hortelã-pimenta"]
        }
        sucesso, dados = tentar_requisicao("post", "http://contraindicacoes:8000/contraindicacoes", json=perfil)
        print("Contraindicações:", dados if sucesso else "Indisponível.")

        time.sleep(5)

if __name__ == "__main__":
    executar_cliente()
