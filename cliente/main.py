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

        sucesso, dados = tentar_requisicao("get", "http://catalogo:5000/oleos")
        if sucesso:
            print("Catálogo:", dados)
        else:
            print("Catálogo indisponível.")

        sintomas = ["ansiedade", "insônia"]
        sucesso, dados = tentar_requisicao("post", "http://recomendar:5000/recomendar", json=sintomas)
        if sucesso:
            print("Recomendações:", dados)
        else:
            print("Serviço de recomendações indisponível.")

        mistura = {
            "nome": "Relax Mix",
            "oleos": ["Lavanda", "Camomila", "Cedro"]
        }
        sucesso, dados = tentar_requisicao("post", "http://misturas:5000/misturas", json=mistura)
        if sucesso:
            print("Mistura criada:", dados)
        else:
            print("Falha ao criar mistura.")

        sucesso, dados = tentar_requisicao("get", "http://misturas:5000/misturas")
        if sucesso:
            print("Misturas salvas:", dados)
        else:
            print("Serviço de misturas indisponível.")

        perfil = {
            "perfil": ["gravidez", "epilepsia"],
            "oleos": ["Lavanda", "Alecrim", "Canela", "Hortelã-pimenta"]
        }
        sucesso, dados = tentar_requisicao("post", "http://contraindicacoes:5000/verificar", json=perfil)
        if sucesso:
            print("Contraindicações:", dados)
        else:
            print("Serviço de contraindicações indisponível.")

        time.sleep(5)

if __name__ == "__main__":
    executar_cliente()
