from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Unidad(Base):
    __tablename__ = 'unidades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo = Column(String)
    coste_oro = Column(Integer)