import pandas as pd
import numpy as np

class EstadisticaBase:
    """
    Clase base para todos los tipos de análisis estadístico.
    Define estructura, validaciones y métodos esenciales.
    """

    def __init__(self, datos):
        """
        Constructor que recibe los datos y los normaliza a una Serie de Pandas.
        """
        # Validar que los datos no estén vacíos
        if datos is None or (isinstance(datos, (list, tuple)) and not datos):
            raise ValueError("La lista de datos no puede estar vacía.")
            
        # Normalizar los datos a una Serie de Pandas
        if isinstance(datos, (list, tuple)):
            self._datos = pd.Series(datos)
        elif isinstance(datos, pd.Series):
            self._datos = datos
        else:
            raise TypeError("El formato de datos debe ser lista, tupla o pd.Series.")

# -------------------------------------------------------------
# Métodos de acceso y control
# -------------------------------------------------------------

    def obtener_datos(self):
        """Devuelve los datos almacenados como Serie de Pandas."""
        return self._datos

    def obtener_n_observaciones(self):
        """Devuelve el número de observaciones no nulas."""
        return self._datos.dropna().shape[0]

# -------------------------------------------------------------
# Métodos estadísticos
# -------------------------------------------------------------

    def contar_datos(self):
        """Devuelve la cantidad total de datos (incluyendo valores nulos)."""
        return len(self._datos)

    def suma(self):
        """Calcula la suma total de los datos (ignorando valores nulos)."""
        total = 0
        for valor in self._datos.dropna():
            total += valor
        return total

    def media(self):
        """Calcula la media aritmética sin usar funciones externas."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return float('nan')
        return self.suma() / n

    def mediana(self):
        """Calcula la mediana ordenando los datos manualmente."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return float('nan')
        
        datos_ordenados = sorted(self._datos.dropna())
        mitad = n // 2

        # Si el número de datos es par, se promedian los dos valores centrales
        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]

    def moda(self):
        """Calcula la moda sin usar librerías externas."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return []
        
        frecuencias = {}
        for valor in self._datos.dropna():
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
        
        max_freq = max(frecuencias.values())
        
        # Si todos los valores son únicos, no existe moda
        if max_freq == 1 and n > 1:
            return []
        
        modas = [k for k, v in frecuencias.items() if v == max_freq]
        return modas if len(modas) > 1 else modas[0]

    def varianza(self):
        """Calcula la varianza muestral sin usar funciones externas."""
        n = self.obtener_n_observaciones()
        if n < 2:
            return float('nan')
            
        media = self.media()
        suma_cuadrados = sum((valor - media) ** 2 for valor in self._datos.dropna())
        return suma_cuadrados / (n - 1)

    def desviacion_estandar(self):
        """Calcula la desviación estándar a partir de la varianza."""
        var = self.varianza()
        return np.sqrt(var)

    def rango(self):
        """Calcula el rango (diferencia entre el valor máximo y el mínimo)."""
        n = self.obtener_n_observaciones()
        if n == 0:
            return float('nan')
        datos_validos = self._datos.dropna()
        return datos_validos.max() - datos_validos.min()
        
    def coeficiente_variacion(self):
        """Calcula el Coeficiente de Variación de Pearson (en %)."""
        media = self.media()
        desv_est = self.desviacion_estandar()

        if np.isnan(media) or np.isnan(desv_est):
            return float('nan')
        
        if media == 0:
            return 0.0 if desv_est == 0 else float('inf')
            
        return (desv_est / media) * 100

# -------------------------------------------------------------
# Resumen general
# -------------------------------------------------------------

    def resumen(self):
        """Genera un resumen con las principales medidas descriptivas."""
        return {
            "Cantidad de datos": self.contar_datos(),
            "Datos válidos": self.obtener_n_observaciones(),
            "Media": self.media(),
            "Mediana": self.mediana(),
            "Moda": self.moda(),
            "Varianza": self.varianza(),
            "Desviación estándar": self.desviacion_estandar(),
            "Rango": self.rango(),
            "Coeficiente de variación (%)": self.coeficiente_variacion()
        }


# -------------------------------------------------------------
# Ejemplo de uso
# -------------------------------------------------------------

#if __name__ == "__main__":
#    datos = [5, 8, 12, 5, 7, 9, 8, 10, 5]
#    analisis = EstadisticaBase(datos)
    
#    print("---- RESUMEN ESTADÍSTICO ----")
#    for k, v in analisis.resumen().items():
#        print(f"{k}: {v}")
