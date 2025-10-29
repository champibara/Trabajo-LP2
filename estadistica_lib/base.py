# estadistica_lib/base.py

import pandas as pd

class DatosBase:
    """Clase base para el manejo de datos estadísticos. Maneja la carga inicial del archivo."""

    def __init__(self, ruta_archivo, columna_interes):
        
        # Se asume que el separador puede ser ';' o ',' e intenta cargar el archivo.
        try:
            self.df = pd.read_csv(ruta_archivo, sep=';')
        except Exception:
            self.df = pd.read_csv(ruta_archivo, sep=',')
            
        self.columna = columna_interes
        
        # Se verifica que la columna de interés exista en el DataFrame.
        if self.columna not in self.df.columns:
            raise ValueError(f"La columna '{self.columna}' no se encuentra en el archivo.")

        # Se guarda la serie de datos relevante, eliminando valores nulos (NaN).
        self.datos = self.df[self.columna].dropna()

    def mostrar_info(self):
        """Muestra información básica de la columna seleccionada."""
        print(f"\n--- Información de la Columna: {self.columna} ---")
        print(f"Tipo de dato: {self.datos.dtype}")
        print(f"Número total de registros (sin NaNs): {len(self.datos)}")
