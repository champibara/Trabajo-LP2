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

    def percentil(self, p):
        """
        Calcula el percentil indicado usando interpolación lineal. 
        Parámetros:
            p (float): Percentil deseado (valor entre 0 y 100).
        """
        # Validación del rango del percentil
        if not (0 <= p <= 100):
            raise ValueError("El percentil debe estar entre 0 y 100.")

        # Elimina valores nulos y ordena los datos
        datos_ordenados = sorted(self.datos.dropna())
        n = self.contar_datos()

        # Si no hay datos válidos, retorna NaN
        if n == 0:
            return float('nan')

        # Posición teórica dentro del conjunto ordenado
        k = (p / 100) * (n - 1)

        # Índices inferior (f) y superior (c)
        f = int(np.floor(k))
        c = int(np.ceil(k))

        # Si ambos índices son iguales, el percentil coincide con ese valor
        if f == c:
            return datos_ordenados[f]
        
        # Interpolación lineal entre los valores vecinos
        return datos_ordenados[f] + (k - f) * (datos_ordenados[c] - datos_ordenados[f])
