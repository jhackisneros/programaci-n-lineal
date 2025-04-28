import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from recursos.oro import Oro

class Poder:
    @staticmethod
    def calcular_poder(dataframe):
        dataframe['poder_total'] = dataframe['cantidad'] * dataframe['poder_unitario']
        return dataframe['poder_total'].sum()

    @staticmethod
    def graficar_poder(dataframe):
        plt.bar(dataframe['unidad'], dataframe['poder_total'])
        plt.xlabel('Unidad')
        plt.ylabel('Poder Total')
        plt.title('Poder total por tipo de unidad')
        plt.show()

if __name__ == "__main__":
    data = {
        'unidad': ['Espadachin', 'Arquero', 'Jinete'],
        'cantidad': [6, 0, 6],
        'poder_unitario': [70, 95, 230]
    }
    df = pd.DataFrame(data)
    total_poder = Poder.calcular_poder(df)
    print(f"Poder total del ejercito: {total_poder}")
    print("Oro por unidad:", Oro.obtener_oro_unidades())
    Poder.graficar_poder(df)