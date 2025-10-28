import pandas as pd
import numpy as np

class EstadisticaBase:
    """
    Clase base abstracta para todos los tipos de análisis estadístico.
    Define la estructura básica, validaciones y encapsulamiento.
    """
    def __init__(self, datos):
        """
        Constructor que recibe los datos y los normaliza a una Serie de Pandas.
        """
        if datos is None or (isinstance(datos, (list, tuple)) and not datos):
            raise ValueError("La lista de datos no puede estar vacía.")
            
        # Normalizar datos a pd.Series
        if isinstance(datos, (list, tuple)):
            self.datos = pd.Series(datos)
        elif isinstance(datos, pd.Series):
            self.datos = datos
        else:
            raise TypeError("El formato de datos debe ser lista, tupla o pd.Series.")

        # Atributo de encapsulamiento
        self._n_observaciones = len(self.datos.dropna())

    # Método abstracto de resumen
    def resumen(self):
        """
        Método que proporciona un resumen de las métricas clave.
        Debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("Las clases hijas deben implementar el método resumen()")
        
    # Métodos para acceder a datos encapsulados
    def obtener_datos(self):
        """Devuelve los datos de la Serie de Pandas."""
        return self.datos

    def obtener_n_observaciones(self):
        """Devuelve el número de observaciones no nulas."""
        return self._n_observaciones

#------------------------------------------------------------
# Métodos Estadísticos
#------------------------------------------------------------

    def contar_datos(self):
        """Devuelve la cantidad total de datos (incluyendo valores nulos si existen)."""
        return len(self.datos)

    def suma(self):
        """Calcula la suma total de los datos sin usar funciones integradas de Python."""
        total = 0
        for valor in self.datos.dropna():
            total += valor
        return total

    def media(self):
        """Calcula la media aritmética sin usar funciones externas."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return float('nan')
        return self.suma() / n

    def mediana(self):
        """Calcula la mediana ordenando los datos manualmente."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return float('nan')
        
        datos_ordenados = sorted(self.datos.dropna())
        mitad = n // 2

        # Si el número de datos es par, promedio de los dos centrales
        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]

    def moda(self):
        """Calcula la moda sin usar librerías externas."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return []
        
        frecuencias = {}
        for valor in self.datos.dropna():
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
        
        max_freq = max(frecuencias.values())
        
        # Si todos los valores son únicos, no hay moda
        if max_freq == 1 and n > 1:
            return []
        
        modas = [k for k, v in frecuencias.items() if v == max_freq]
        return modas if len(modas) > 1 else modas[0]
