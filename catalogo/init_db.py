from app import Session, OleoModel

oleos_iniciais = [
    {"nome": "Lavanda", "beneficios": "calmante;relaxante;auxilia no sono"},
    {"nome": "Hortelã-pimenta", "beneficios": "revigorante;alivia dores de cabeça;descongestionante"},
    {"nome": "Tea Tree", "beneficios": "antisséptico;antifúngico;cicatrizante"},
]

db = Session()

for oleo in oleos_iniciais:
    existente = db.query(OleoModel).filter_by(nome=oleo["nome"]).first()
    if not existente:
        novo = OleoModel(**oleo)
        db.add(novo)

db.commit()
db.close()
