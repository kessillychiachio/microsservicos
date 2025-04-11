from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Mistura(Base):
    __tablename__ = "misturas"
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, index=True)
    oleos = relationship("Oleo", back_populates="mistura", cascade="all, delete")

class Oleo(Base):
    __tablename__ = "oleos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    mistura_id = Column(Integer, ForeignKey("misturas.id"))
    mistura = relationship("Mistura", back_populates="oleos")
