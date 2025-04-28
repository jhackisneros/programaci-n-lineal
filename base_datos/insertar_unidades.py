from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_datos.modelos import Unidad

class InsertarUnidades:
    @staticmethod
    def insertar(nombre_db='unidades.db'):
        engine = create_engine(f"sqlite:///{nombre_db}")
        Session = sessionmaker(bind=engine)
        session = Session()

        unidades = [
            Unidad(nombre="Espadachín", tipo="Infantería", coste_oro=0),
            Unidad(nombre="Arquero", tipo="A distancia", coste_oro=40),
            Unidad(nombre="Jinete", tipo="Caballería", coste_oro=100)
        ]

        session.add_all(unidades)
        session.commit()
        session.close()

        print("Unidades insertadas correctamente.")

if __name__ == "__main__":
    InsertarUnidades.insertar()