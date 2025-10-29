# estadistica_lib/cuantitativos.py

# Se importa la Clase Padre (DatosBase) para implementar Herencia.
from .base import DatosBase
import pandas as pd
# Se agregan las librerías para gráficos y manejo de rutas.
import matplotlib.pyplot as plt 
import os 

# Se definen las constantes de ruta para guardar archivos.
DIR_TABLAS = 'tablas'
DIR_GRAFICOS = 'graficos'

class DatosCuantitativos(DatosBase):
    """Clase para el cálculo de estadísticas y generación de histogramas para datos cuantitativos."""

    def __init__(self, ruta_archivo, columna_interes):
        # Se llama al constructor de la clase base (DatosBase).
        super().__init__(ruta_archivo, columna_interes)
        
        # Se intenta convertir la serie de datos a tipo numérico para asegurar cálculos.
        try:
            self.datos = pd.to_numeric(self.datos)
        except Exception:
            print(f"Advertencia: Los datos en '{self.columna}' no son puramente numéricos.")
            
        print(f"Datos Cuantitativos cargados para: {self.columna}")


    def calcular_resumen(self):
        """Calcula las estadísticas básicas: media, mediana, moda, desv. estándar y cuartiles."""
        
        # Se calculan las medidas de tendencia central y dispersión.
        media = self.datos.mean().round(2)
        mediana = self.datos.median().round(2)
        moda = self.datos.mode().tolist()
        desv_estandar = self.datos.std().round(2)
        
        # Se calculan los percentiles (Cuartil 1 y Cuartil 3).
        q1 = self.datos.quantile(0.25).round(2)
        q3 = self.datos.quantile(0.75).round(2)

        # Se retorna el resumen como un diccionario.
        resumen = {
            'Media (Promedio)': media,
            'Mediana': mediana,
            'Moda(s)': moda,
            'Desviación Estándar': desv_estandar,
            'Cuartil 1 (P25)': q1,
            'Cuartil 3 (P75)': q3
        }
        return resumen

    def guardar_resumen_estadistico(self, nombre_archivo):
        """Se calcula el resumen estadístico y se guarda en un archivo CSV."""
        resumen = self.calcular_resumen()
        
        # Se convierte el diccionario de resumen a DataFrame para guardarlo.
        resumen_df = pd.DataFrame(resumen.items(), columns=['Estadística', 'Valor'])

        # Se construye la ruta de guardado dentro de la carpeta 'tablas'.
        ruta_completa = os.path.join(DIR_TABLAS, nombre_archivo)
        
        # Se guarda el DataFrame en formato CSV.
        resumen_df.to_csv(ruta_completa, index=False)
        print(f"✅ Resumen estadístico guardado en: {ruta_completa}")

    def generar_y_guardar_histograma(self, nombre_archivo):
        """Se genera un histograma para la distribución de datos y se guarda en PNG."""
        
        plt.figure(figsize=(10, 6))
        self.datos.plot(kind='hist', bins=10, edgecolor='black', alpha=0.7)
        plt.title(f'Histograma de {self.columna}')
        plt.xlabel(self.columna)
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', alpha=0.5)
        plt.tight_layout()
        
        # Se construye la ruta de guardado dentro de la carpeta 'graficos'.
        ruta_completa = os.path.join(DIR_GRAFICOS, nombre_archivo)
        plt.savefig(ruta_completa)
        plt.close()
        print(f"✅ Histograma guardado en: {ruta_completa}")
