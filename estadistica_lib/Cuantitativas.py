from base import EstadisticaBase
import numpy as np
import math

class MedidasCuantitativas(EstadisticaBase):
    """
    Clase derivada de EstadisticaBase que incorpora medidas 
    específicas para variables cuantitativas.
    """

    def __init__(self, datos):
        """
        Inicializa la clase con los datos numéricos y hereda 
        los atributos y métodos básicos de EstadisticaBase.
        
        Parámetros:
            datos (list o array): Conjunto de valores numéricos.
        """
        super().__init__(datos)  # Hereda métodos y atributos de la clase base

    # ---------------------------------------------------------
    #                      MEDIDAS DE POSICIÓN
    # ---------------------------------------------------------
    def cuartiles(self):
        """
        Calcula los cuartiles Q1, Q2 (mediana) y Q3 de los datos.
        """
        # Se ordenan los datos de menor a mayor
        datos_ordenados = sorted(self.datos)
        n = self.contar_datos()
        mitad = n // 2

        # Q2 se obtiene reutilizando el método 'mediana' de la clase base
        Q2 = self.mediana()

        # Si el número de datos es par o impar, cambia la forma de dividir
        if n % 2 == 0:
            Q1 = np.median(datos_ordenados[:mitad])
            Q3 = np.median(datos_ordenados[mitad:])
        else:
            Q1 = np.median(datos_ordenados[:mitad])
            Q3 = np.median(datos_ordenados[mitad + 1:])

        # Se devuelven los tres cuartiles en un diccionario
        return {"Q1": Q1, "Q2": Q2, "Q3": Q3}

