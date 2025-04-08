import requests

print ("Catálogo de Óleos Essenciais:")
res = requests.get("http://localhost:5001/oleos")
print (res.json())

print ("Recomendação por sintomas:")
res = requests.post("http://localhost:5002/recomendar")
print (res.json())

print ("\n Criar mistura personalizada:")
mistura = {
  "nome": "Calmante e relaxante",
  "oleos": ["Lavanda", "Camomila", "Cedro"]
  }
res = requests.post("http://localhost:5003/misturas", json=mistura)
print (res.json())

print ("Misturas salvas:")
res = requests.get("http://localhost:5003/misturas")
print (res.json())

print ("Verificar contraindicações:")
perfil = {
  "perfil": ["gravidez", "epilepsia"],
  "oleos": ["Lavanda", "Alecrim", "Canela", "Hortelã-pimenta"]
}
res = requests.get("http://localhost:5004/verificar", json=perfil)
print (res.json())
