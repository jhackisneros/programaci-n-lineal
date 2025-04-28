from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Unidad(Base):
    __tablename__ = 'unidades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    coste_oro = Column(Integer)