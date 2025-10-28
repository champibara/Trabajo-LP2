import pandas as pd
import numpy as np

class EstadisticaBase:
    """
    Clase base para operaciones estadísticas genéricas.
    Las clases hijas (como DatosCualitativos) heredan de esta.
    """
    def __init__(self, datos):
        self.datos = pd.Series(datos)

    def obtener_n_observaciones(self):
        """Devuelve el número de observaciones válidas (no nulas)."""
        return self.datos.dropna().shape[0]


class DatosCualitativos(EstadisticaBase):
    """
    Clase para analizar variables cualitativas.
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

        # Cargar archivo CSV
        try:
            df = pd.read_csv(ruta_archivo, sep=separador)
        except FileNotFoundError:
            raise FileNotFoundError(f"Archivo no encontrado en la ruta: {ruta_archivo}")

        # Validar que la columna exista
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el archivo.")

        # Inicializa clase base con la columna seleccionada
        super().__init__(df[columna].astype(str))

        # Convertir los datos a tipo categórico
        self.datos = self.datos.astype("category")

    def calcular_moda(self):
        """
        Calcula la moda para la variable categórica.
        Returns:
            dict: Moda(s) y su frecuencia.
        """
        conteo = self.datos.value_counts()
        max_freq = conteo.max()
        modas = conteo[conteo == max_freq].index.tolist()
        return {"Moda": modas, "Frecuencia": int(max_freq)}

    def tabla_frecuencia(self):
        """
        Genera la tabla de frecuencias: Absoluta, Relativa, y Acumulada.
        Returns:
            list[dict]: Tabla de frecuencias lista para convertir a JSON o imprimir.
        """
        conteo = self.datos.value_counts().sort_index()
        fr = (conteo / conteo.sum()).round(4)

        tabla_df = pd.DataFrame({
            "Frecuencia_Absoluta": conteo,
            "Frecuencia_Relativa": (fr * 100).map("{:.2f}%".format),
            "Frecuencia_Absoluta_Acumulada": conteo.cumsum(),
            "Frecuencia_Relativa_Acumulada": ((fr.cumsum()) * 100).map("{:.2f}%".format)
        })

        return tabla_df.reset_index(names=self.nombre_columna).to_dict("records")

    def resumen(self):
        """
        Devuelve un resumen completo del análisis de la variable cualitativa.
        Returns:
            dict: Información resumida.
        """
        res = {
            "Tipo_Dato": "Cualitativo / Categórico",
            "Variable": self.nombre_columna,
            "Observaciones_Validas": self.obtener_n_observaciones(),
            "Datos_Nulos": int(self.datos.isna().sum()),
            "Número_Categorías": int(self.datos.nunique()),
            "Moda": self.calcular_moda(),
            "Tabla_Frecuencias": self.tabla_frecuencia()
        }
        return res
# ==========================
# ✅ EJEMPLO DE USO
# ==========================
if __name__ == "__main__":
    archivo = "Alumnos Matriculados 2025-II-UNALM.csv"   # reemplazándolo por el archivo csv
    columna = "Curso"      # ejemplo de columna cualitativa

    analisis = DatosCualitativos(archivo, columna, separador=';')
    resumen = analisis.resumen()

    # Mostrar resumen
    import pprint
    pprint.pprint(resumen)