from sqlalchemy import Column, Integer, String
from database import Base

class Sugestao(Base):
    __tablename__ = "sugestoes"
    id = Column(Integer, primary_key=True)
    sintoma = Column(String, index=True)
    oleo = Column(String)
