from .cuantitativos import DatosCuantitativos
from .base import DatosBase

from scipy import stats
import numpy as np
import pandas as pd
import os
from .cuantitativos import DIR_TABLAS

class InferenciaEstadistica(DatosCuantitativos):
    
    def __init__(self, ruta_archivo, columna_interes):
        super().__init__(ruta_archivo, columna_interes)
        self._n = len(self.datos)
        
        if self._n < 2:
            raise ValueError("Se requieren al menos 2 observaciones para la inferencia.")
            
        print(f"Módulo de Inferencia Estadística cargado para: {self.columna}")

    def intervalo_confianza_media(self, nivel_confianza=0.95):
        resumen = self.calcular_resumen()
        media = resumen['Media (Promedio)']
        desv_estandar = resumen['Desviación Estándar']
        n = self._n
        
        if n < 2:
            return {"Error": "Se requieren al menos 2 observaciones para el IC."}
        
        grados_libertad = n - 1

        t_critico = stats.t.ppf(1 - (1 - nivel_confianza) / 2, grados_libertad)
        
        error_estandar = desv_estandar / (n ** 0.5)
        
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
        
    def prueba_z_media_poblacional(self, media_hipotetica, desv_estandar_poblacional, nivel_significancia=0.05):
        resumen = self.calcular_resumen()
        media_muestral = resumen['Media (Promedio)']
        n = self._n

        if n < 1:
            return {"Error": "Se requiere al menos 1 observación."}
        if desv_estandar_poblacional <= 0:
            return {"Error": "La desviación estándar poblacional debe ser positiva."}
        
        error_estandar = desv_estandar_poblacional / np.sqrt(n)

        Z_stat = (media_muestral - media_hipotetica) / error_estandar
        
        p_value = 2 * (1 - stats.norm.cdf(np.abs(Z_stat)))
        
        conclusion = "No se rechaza H0 (No hay diferencia significativa)"
        if p_value < nivel_significancia:
            conclusion = "Se rechaza H0 (Existe diferencia significativa)"
        return {
            "Prueba": "Prueba Z para la Media (σ conocido)",
            "Z_Estadístico": Z_stat.round(4),
            "Media_Hipotética (μ0)": media_hipotetica,
            "P_Valor": p_value.round(4),
            "Conclusion": conclusion
        }
