#Importamos los paquetes y la clase padre a utilizar
import pandas as pd
from scipy import stats 
import numpy as np
from base import EstadisticaBase

#Creación de clase
class InferenciaEstadistica(EstadisticaBase):
    """
    Clase hija para realizar inferencia estadística avanzada (Pruebas de Hipótesis e ICs)
    heredando los cálculos de la media y la varianza.
    """
    def __init__(self, datos):
        """Inicializa la clase base."""
        super().__init__(datos)
        self._n = self.obtener_n_observaciones()
        
        if self._n < 2:
             # Dejamos pasar para permitir pruebas con dos muestras
             pass

