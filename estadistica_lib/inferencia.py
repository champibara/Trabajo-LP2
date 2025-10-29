# Importamos los paquetes y la clase padre a utilizar

from .cuantitativos import DatosCuantitativos # Se importa la clase padre
from .base import DatosBase # Se importa la base para chequeos de tipo
from scipy import stats 
import numpy as np
import pandas as pd
import os 
# Se reutilizan las constantes definidas en cuantitativos.py
from .cuantitativos import DIR_TABLAS

class InferenciaEstadistica(DatosCuantitativos):
    """
    Clase para realizar pruebas de hipótesis (t, F) e Intervalos de Confianza (IC)
    para datos cuantitativos. Hereda los cálculos descriptivos de DatosCuantitativos.
    """
    
    def __init__(self, ruta_archivo, columna_interes):
        """Inicializa la clase llamando al constructor de DatosCuantitativos."""
        super().__init__(ruta_archivo, columna_interes)
        self._n = len(self.datos)
        
        if self._n < 2:
             raise ValueError("Se requieren al menos 2 observaciones para la inferencia.")
             
        print(f"Módulo de Inferencia Estadística cargado para: {self.columna}")
