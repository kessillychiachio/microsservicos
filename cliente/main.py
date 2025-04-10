import requests
import time

def tentar_requisicao(metodo, url, tentativas = 3, **kwargs):
  for tentativa in range(tentativas):
    try:
      res = getattr(requests, metodo) (url, **kwargs)
      return res.json()
    except Exception as e:
      print(f"Tentativa {tentativa + 1} falhou para {url}: {e}")
      time.sleep(2)
  return f"Erro ao acessar {url} após {tentativas} tentativas."    

def menu():
  while True:
    print("\nMenu principal")
    print("1. Catálogo de óleos")
    print("2. Recomendações por sintomas")
    print("3. Criar mistura personalizada")
    print("4. Verificar contraindicações")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
      print(tentar_requisicao("get", "http://catalogo:5000/oleos"))
    
    elif opcao == "2":
      sintomas = input("Digite os sintomas separados por vírgula: ").split(",")
      sintomas = [sintoma.strip() for sintoma in sintomas]
      print(tentar_requisicao("post", "http://recomendar:5000/recomendar"))
      
    elif opcao == "3":
      nome = input("Digite o nome da mistura: ")
      oleos = input("Digite os óleos separados por vírgula: ").split(",")
      oleos = [oleo.strip() for oleo in oleos]
      mistura = {"nome": nome, "oleos": oleos}
      print (tentar_requisicao("post", "http://misturas:5000/misturas", json=mistura))
      
    elif opcao == "4":
      print(tentar_requisicao("get", "http://misturas:5000/misturas"))
      
    elif opcao == "5":
      perfil = input ("Informe os perfis (ex: gravidez, epilepsia) separados por vírgula: ").split(",")
      oleos = input ("Oleos separados por vírgula: ").split(",")
      dados = {
        "perfil" = [perfil.strip() for perfil in perfil],
        "oleos" = [oleo.strip() for oleo in oleos]
      }
      print(tentar_requisicao("post", "http://contraindicacoes:5000/verificar", json=dados))
      
    elif opcao == "0":
      print("Saindo do programa.")
      break
    else:
      print("Opção inválida. Tente novamente.")
      
menu()
    
    
  
print("Catálogo de Óleos Essenciais:")
print(tentar_requisicao("get", "http://catalogo:5000/oleos"))

print("\nRecomendação por sintomas:")
print(tentar_requisicao("post", "http://recomendar:5000/recomendar"))

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
