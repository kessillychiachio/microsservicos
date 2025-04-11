from database import Session, engine, Base
from models import Sugestao

Base.metadata.create_all(bind=engine)

def popular_dados():
    sugestoes_iniciais = {
        "ansiedade": ["Lavanda", "Camomila", "Bergamota"],
        "insônia": ["Lavanda", "Manjerona", "Cedro"],
        "estresse": ["Hortelã-pimenta", "Ylang Ylang", "Laranja-selvagem"]
    }

    db = Session()
    if db.query(Sugestao).count() == 0:
        for sintoma, oleos in sugestoes_iniciais.items():
            for oleo in oleos:
                db.add(Sugestao(sintoma=sintoma.lower(), oleo=oleo))
        db.commit()
        print("Sugestões populadas no banco!")
    else:
        print("Banco já possui sugestões.")
    db.close()

popular_dados()
