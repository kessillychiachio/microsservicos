from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, index=True)
    oleos = relationship("OleoContraindicado", back_populates="perfil", cascade="all, delete")

class OleoContraindicado(Base):
    __tablename__ = "oleos_contraindicados"
    id = Column(Integer, primary_key=True)
    oleo = Column(String)
    perfil_id = Column(Integer, ForeignKey("perfis.id"))
    perfil = relationship("Perfil", back_populates="oleos")
