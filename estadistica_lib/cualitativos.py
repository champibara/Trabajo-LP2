import pandas as pd
from .base import EstadisticaBase

class DatosCualitativos(EstadisticaBase):
    """
    Clase para analizar variables cualitativas o categóricas.
    Hereda de EstadisticaBase y aplica Polimorfismo.
    """

    def __init__(self, ruta_archivo, columna, separador=';'):
        """
        Inicializa la clase leyendo un archivo CSV y seleccionando la columna a analizar.
        
        Args:
            ruta_archivo (str): Ruta del archivo CSV.
            columna (str): Nombre de la columna cualitativa.
            separador (str): Delimitador del archivo (por defecto ';').
        """
        # Cargar el archivo
        try:
            df = pd.read_csv(ruta_archivo, sep=separador)
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo no encontrado en la ruta: {ruta_archivo}")

        # Validar la existencia de la columna
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el archivo.")

        # Llamar al constructor de la clase base con los datos seleccionados
        super().__init__(df[columna].astype(str))  # Se guardan los datos como texto
        self._nombre_columna = columna

        # Convertir los datos a tipo categórico
        self._datos = self._datos.astype('category')

    # -------------------------------------------------------------
    # Métodos específicos para variables cualitativas
    # -------------------------------------------------------------

    def calcular_moda(self):
        """
        Calcula la moda (valor o valores más frecuentes).
        Returns:
            str | list: La(s) categoría(s) con mayor frecuencia.
        """
        modas = self._datos.mode().tolist()
        return modas[0] if len(modas) == 1 else modas

    def tabla_frecuencia(self):
        """
        Genera una tabla con frecuencias absoluta, relativa y acumulada.
        Returns:
            DataFrame: Tabla de frecuencias.
        """
        fa = self._datos.value_counts(dropna=True)
        fr = self._datos.value_counts(normalize=True, dropna=True).round(4)

        faa = fa.cumsum()
        fra = fr.cumsum().round(4)

        tabla = pd.DataFrame({
            "Frecuencia_Absoluta": fa,
            "Frecuencia_Relativa (%)": fr * 100,
            "Frecuencia_Absoluta_Acumulada": faa,
            "Frecuencia_Relativa_Acumulada (%)": fra * 100
        })

        tabla.index.name = self._nombre_columna
        tabla.reset_index(inplace=True)
        return tabla

    # -------------------------------------------------------------
    # Polimorfismo: redefinición de resumen()
    # -------------------------------------------------------------

    def resumen(self):
        """
        Genera un resumen general de la variable cualitativa.
        Returns:
            dict: Resumen con la moda y la tabla de frecuencias.
        """
        return {
            "Tipo de Dato": "Cualitativo / Categórico",
            "Variable": self._nombre_columna,
            "Observaciones Válidas": self.obtener_n_observaciones(),
            "Moda": self.calcular_moda(),
            "Tabla de Frecuencias": self.tabla_frecuencia().to_dict(orient='records')
        }
