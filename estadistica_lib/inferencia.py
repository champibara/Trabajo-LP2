# Importamos los paquetes y la clase padre a utilizar

from .cuantitativos import DatosCuantitativos # Se importa la clase padre
from .base import DatosBase # Se importa la base para chequeos de tipo
from scipy import stats 
import numpy as np
import pandas as pd
import os 
# Se reutilizan las constantes definidas en cuantitativos.py
from .cuantitativos import DIR_TABLAS

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
# --- Pruebas de Hipótesis (Dos Muestras) ---

    def prueba_f_varianzas(self, otra_muestra, nivel_significancia=0.05):
        """
        Prueba F (Fisher) para comparar si dos poblaciones tienen varianzas iguales.
        
        H0: sigma1^2 = sigma2^2
        Ha: sigma1^2 != sigma2^2 (Prueba de dos colas)
        """
        if not isinstance(otra_muestra, EstadisticaBase):
            raise TypeError("La otra_muestra debe ser una instancia de EstadisticaBase o una clase hija.")
        
        try:
            var1 = self.varianza()
            var2 = otra_muestra.varianza()
        except TypeError:
             raise TypeError("La prueba F requiere que ambas muestras sean numéricas.")
             
        n1 = self._n
        n2 = otra_muestra.obtener_n_observaciones()
        
        if n1 < 2 or n2 < 2:
            return {"Error": "Se requieren al menos 2 obs. en cada muestra."}
