import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_datos.modelos import Base, Unidad

DB_PATH = 'unidades.db'

def crear_base_datos():
    if not os.path.exists(DB_PATH):
        engine = create_engine(f"sqlite:///{DB_PATH}")
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        unidades = [
            Unidad(nombre="Espadachin", coste_oro=0),
            Unidad(nombre="Arquero", coste_oro=40),
            Unidad(nombre="Jinete", coste_oro=100),
        ]

        session.add_all(unidades)
        session.commit()
        session.close()
        print("Base de datos creada exitosamente.")
    else:
        print("La base de datos ya existe.")

if __name__ == "__main__":
    crear_base_datos()