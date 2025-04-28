from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_datos.modelos import Unidad

class Oro:
    ORO_TOTAL = 600

    @classmethod
    def obtener_oro(cls):
        return cls.ORO_TOTAL

    @staticmethod
    def obtener_oro_unidades(nombre_db='unidades.db'):
        engine = create_engine(f"sqlite:///{nombre_db}")
        Session = sessionmaker(bind=engine)
        session = Session()

        unidades = session.query(Unidad).all()
        oro_por_unidad = {unidad.nombre: unidad.coste_oro for unidad in unidades}
        session.close()
        return oro_por_unidad