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
    # --- Métodos de Inferencia Unimuestra ---
    
    def intervalo_confianza_media(self, nivel_confianza=0.95):
        """
        Calcula el Intervalo de Confianza (IC) para la media poblacional (mu).
        Utiliza la distribución t de Student.
        """
        # Obtenemos métricas de la clase padre (DatosCuantitativos)
        resumen = self.calcular_resumen()
        media = resumen['Media (Promedio)']
        desv_estandar = resumen['Desviación Estándar']
        n = self._n
        
        grados_libertad = n - 1
        
        # Valor crítico t de Student: ppf (percent point function = inversa de la CDF)
        t_critico = stats.t.ppf(1 - (1 - nivel_confianza) / 2, grados_libertad)
        
        # Error Estándar de la Media
        error_estandar = desv_estandar / (n ** 0.5)
        
        # Margen de Error
        margen_error = t_critico * error_estandar
        
        limite_inferior = media - margen_error
        limite_superior = media + margen_error
        
        return {
            'IC_Nivel': nivel_confianza,
            'Media_Muestral': media,
            'Margen_Error': margen_error,
            'Limite_Inferior': limite_inferior.round(4),
            'Limite_Superior': limite_superior.round(4)
        }
