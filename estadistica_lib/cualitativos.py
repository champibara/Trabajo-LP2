# estadistica_lib/cualitativos.py

# Se importa la Clase Padre (DatosBase) para implementar Herencia.
from .base import DatosBase
import pandas as pd
# Se agregan las librerías para gráficos y manejo de rutas.
import matplotlib.pyplot as plt 
import os 

# Se definen las constantes de ruta para guardar archivos.
DIR_TABLAS = 'tablas'
DIR_GRAFICOS = 'graficos'

class DatosCualitativos(DatosBase):
    """Clase para el cálculo de estadísticas y generación de tablas/gráficos para datos cualitativos."""

    def __init__(self, ruta_archivo, columna_interes):
        # Se llama al constructor de la clase base (DatosBase).
        super().__init__(ruta_archivo, columna_interes)
        print(f"Datos Cualitativos cargados para: {self.columna}")

    def calcular_frecuencias(self):
        """Calcula la tabla de frecuencias (Fa y Fr)."""
        
        # Se calcula la Frecuencia Absoluta (Fa).
        frec_abs = self.datos.value_counts().sort_index()
        
        # Se calcula la Frecuencia Relativa (Fr) y se convierte a porcentaje.
        frec_rel = self.datos.value_counts(normalize=True).sort_index()
        frec_rel_perc = (frec_rel * 100).round(2).astype(str) + '%'

        # Se genera el DataFrame de la tabla de frecuencia.
        tabla_frecuencia = pd.DataFrame({
            'Frecuencia Absoluta (Fa)': frec_abs,
            'Frecuencia Relativa (%)': frec_rel_perc
        })

        return tabla_frecuencia

    def calcular_moda(self):
        """Calcula la moda (o modas)."""
        return self.datos.mode().tolist()

    def guardar_tabla_frecuencias(self, nombre_archivo):
        """Se calcula y se guarda la tabla de frecuencias en un archivo CSV."""
        tabla = self.calcular_frecuencias()
        
        # Se construye la ruta de guardado dentro de la carpeta 'tablas'.
        ruta_completa = os.path.join(DIR_TABLAS, nombre_archivo)
        
        # Se guarda el DataFrame en formato CSV.
        tabla.to_csv(ruta_completa, index=True)
        print(f"✅ Tabla de frecuencias guardada en: {ruta_completa}")
        
    def generar_y_guardar_grafico(self, nombre_archivo):
        """Se genera un gráfico de barras de frecuencias y se guarda en PNG."""
        frec_abs = self.datos.value_counts().sort_index()
        
        plt.figure(figsize=(10, 6))
        frec_abs.plot(kind='bar')
        plt.title(f'Frecuencia Absoluta de {self.columna}')
        plt.xlabel(self.columna)
        plt.ylabel('Frecuencia Absoluta')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Se construye la ruta de guardado dentro de la carpeta 'graficos'.
        ruta_completa = os.path.join(DIR_GRAFICOS, nombre_archivo)
        plt.savefig(ruta_completa)
        plt.close() # Se cierra la figura para liberar memoria.
        print(f"✅ Gráfico de barras guardado en: {ruta_completa}")
