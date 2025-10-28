import pandas as pd
import numpy as np
from .base import EstadisticaBase

class DatosCualitativos(EstadisticaBase):
    """
    Clase para analizar variables cualitativas (categóricas).
    Hereda de EstadisticaBase y aplica Polimorfismo.
    """

    def __init__(self, ruta_archivo, columna, separador=';'):
        """
        Inicializa la clase leyendo el archivo CSV y seleccionando la columna.
        
        Args:
            ruta_archivo (str): La ruta al archivo CSV.
            columna (str): El nombre de la columna cualitativa a analizar.
            separador (str): El delimitador del archivo (ej: ';', ',').
        """
        self.ruta_archivo = ruta_archivo
        self.nombre_columna = columna
        
        # Uso de pd.read_csv para la carga inicial (Similar al otro grupo)
        try:
            # Lector de CSV de Pandas
            df = pd.read_csv(ruta_archivo, sep=separador) 
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo no encontrado en la ruta: {ruta_archivo}")
        
        # Validar si la columna existe antes de usarla
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el archivo.")
            
        # Inicializa la clase padre (EstadisticaBase) con la Serie de datos
        super().__init__(df[columna].astype(str))
        
        # Aseguramos que los datos internos son tratados como categóricos
        self.datos = self.datos.astype('category')
        
    def calcular_moda(self):
        """
        Calcula la moda para la variable categórica.
        
        Returns:
            list/str: La(s) categoría(s) con mayor frecuencia.
        """
        modas = self.datos.mode().tolist()
        return modas[0] if len(modas) == 1 else modas

    def tabla_frecuencia(self):
        """
        [C17 Docstring] Genera la tabla de frecuencias: Absoluta, Relativa, y Acumulada.
        """
        # Frecuencia Absoluta y Relativa
        fa = self.datos.value_counts(dropna=True)
        fr = self.datos.value_counts(normalize=True, dropna=True).round(4)
        
        # Frecuencia Acumulada
        faa = fa.cumsum()
        fra = fr.cumsum().round(4)

        tabla_df = pd.DataFrame({
            "Frecuencia_Absoluta": fa,
            "Frecuencia_Relativa": fr,
            "Frecuencia_Absoluta_Acumulada": faa,
            "Frecuencia_Relativa_Acumulada": fra
        })
        
        # Formato de porcentaje
        tabla_df["Frecuencia_Relativa"] = (tabla_df["Frecuencia_Relativa"] * 100).apply(lambda x: f"{x:.2f}%")
        tabla_df["Frecuencia_Relativa_Acumulada"] = (tabla_df["Frecuencia_Relativa_Acumulada"] * 100).apply(lambda x: f"{x:.2f}%")
        
        return tabla_df.reset_index().rename(columns={'index': self.nombre_columna}).to_dict('records')
