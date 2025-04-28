from sqlalchemy import create_engine
from base_datos.modelos import Base

class CrearDB:
    @staticmethod
    def crear_base(nombre_db='unidades.db'):
        engine = create_engine(f"sqlite:///{nombre_db}")
        Base.metadata.create_all(engine)

if __name__ == "__main__":
    CrearDB.crear_base()