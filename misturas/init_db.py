from database import Base, engine
from models import Mistura, Oleo, Antagonico

Base.metadata.create_all(bind=engine)
print("Banco criado com sucesso!")
