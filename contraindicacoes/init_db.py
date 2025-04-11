from database import Session, engine, Base
from models import Perfil, OleoContraindicado

Base.metadata.create_all(bind=engine)

def popular_dados():
    db = Session()
    if db.query(Perfil).count() == 0:
        dados = {
            "gravidez": ["Alecrim", "Canela", "Cravo", "Salvia", "Manjerona", "Gengibre"],
            "epilepsia": ["Alecrim", "Eucalipto", "Hortelã-pimenta"],
            "pressao alta": ["Alecrim", "Tomilho", "Hortelã-pimenta"],
            "pressao baixa": ["Ylang Ylang", "Camomila"]
        }
        for nome, oleos in dados.items():
            perfil = Perfil(nome=nome.strip().lower())
            db.add(perfil)
            db.flush()
            for oleo in oleos:
                db.add(OleoContraindicado(oleo=oleo, perfil_id=perfil.id))
        db.commit()
        print("Banco populado!")
    else:
        print("Banco já tem dados.")
    db.close()

popular_dados()
