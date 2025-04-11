from app import Base, Session, engine, OleoModel

Base.metadata.create_all(bind=engine)

db = Session()

if db.query(OleoModel).count() == 0:
    oleos = [
        ("Lavanda", ["Reduz ansiedade", "Melhora o sono", "Alivia dores de cabeça"]),
        ("Hortelã-Pimenta", ["Melhora concentração", "Alivia dores musculares", "Reduz enjoos"]),
        ("Melaleuca", ["Combate acne", "Antifúngico", "Anti-inflamatório"]),
        ("Alecrim", ["Melhora memória", "Alivia dores", "Fortalece cabelo"]),
        ("Laranja Doce", ["Melhora humor", "Ajuda na digestão", "Promove relaxamento"]),
        ("Eucalipto", ["Descongestionante nasal", "Alivia sintomas de gripe", "Expectorante"]),
        ("Camomila Romana", ["Calmante", "Anti-inflamatório", "Ajuda no sono"]),
        ("Ylang Ylang", ["Reduz estresse", "Afrodisíaco", "Equilibra emoções"]),
    ]

    for nome, beneficios in oleos:
        oleo = OleoModel(nome=nome, beneficios=";".join(beneficios))
        db.add(oleo)

    db.commit()
    print("Banco criado e populado com dados iniciais")
else:
    print("Banco já estava populado, nada a fazer ")

db.close()
