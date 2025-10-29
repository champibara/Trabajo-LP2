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
    # ----------------------------------------------------------------------
    # 1. INFERENCIA UNIMUESTRA: Intervalo de Confianza para la Media
    # ----------------------------------------------------------------------
    
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
    # ----------------------------------------------------------------------
    # 2. PRUEBAS DE HIPÓTESIS: Dos Muestras (t student y F estadístico)
    # ----------------------------------------------------------------------
    
    def prueba_f_varianzas(self, otra_muestra, nivel_significancia=0.05):
        """
        Prueba F para comparar si dos muestras provienen de poblaciones 
        con varianzas iguales (Homocedasticidad).
        """
        if not isinstance(otra_muestra, DatosBase):
            raise TypeError("La otra_muestra debe ser una instancia de DatosBase o una clase hija.")
        
        # Acceso directo a las varianzas del resumen (ya agregada en DatosCuantitativos)
        var1 = self.calcular_resumen()['Varianza']
        var2 = otra_muestra.calcular_resumen()['Varianza']
            
        n1 = self._n
        n2 = otra_muestra.obtener_n_observaciones()
            
        if n1 < 2 or n2 < 2:
            return {"Error": "Se requieren al menos 2 obs. en cada muestra para varianza."}
            
        # Estadístico F (mayor varianza en el numerador)
        if var1 >= var2:
            F_stat = var1 / var2
            df1, df2 = n1 - 1, n2 - 1
        else:
            F_stat = var2 / var1
            df1, df2 = n2 - 1, n1 - 1
        
        # P-valor (prueba de dos colas: 2 * (1 - cdf))
        p_value = 2 * (1 - stats.f.cdf(F_stat, df1, df2))
        
        conclusion = "No se rechaza H0 (Varianzas Iguales)"
        if p_value < nivel_significancia:
            conclusion = "Se rechaza H0 (Varianzas Diferentes)"

        return {
            "Prueba": "Prueba F de Varianzas",
            "F_Estadístico": F_stat.round(4),
            "P_Valor": p_value.round(4),
            "Nivel_Significancia": nivel_significancia,
            "Conclusion": conclusion
        }   