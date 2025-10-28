from base import EstadisticaBase
import numpy as np
import math

class MedidasCuantitativas(EstadisticaBase):
    """
    Clase derivada de EstadisticaBase que incorpora medidas 
    específicas para variables cuantitativas.
    """

    def __init__(self, datos):
        """
        Inicializa la clase con los datos numéricos y hereda 
        los atributos y métodos básicos de EstadisticaBase.
        
        Parámetros:
            datos (list o array): Conjunto de valores numéricos.
        """
        super().__init__(datos)  # Hereda métodos y atributos de la clase base

# ---------------------------------------------------------
# Medidas de posición
# ---------------------------------------------------------
    def cuartiles(self):
        """
        Calcula los cuartiles Q1, Q2 (mediana) y Q3 de los datos.
        """
        # Se ordenan los datos de menor a mayor
        datos_ordenados = sorted(self.datos)
        n = self.contar_datos()
        mitad = n // 2

        # Q2 se obtiene reutilizando el método 'mediana' de la clase base
        Q2 = self.mediana()

        # Si el número de datos es par o impar, cambia la forma de dividir
        if n % 2 == 0:
            Q1 = np.median(datos_ordenados[:mitad])
            Q3 = np.median(datos_ordenados[mitad:])
        else:
            Q1 = np.median(datos_ordenados[:mitad])
            Q3 = np.median(datos_ordenados[mitad + 1:])

        # Se devuelven los tres cuartiles en un diccionario
        return {"Q1": Q1, "Q2": Q2, "Q3": Q3}

    def percentil(self, p):
        """
        Calcula el percentil indicado usando interpolación lineal. 
        Parámetros:
            p (float): Percentil deseado (valor entre 0 y 100).
        """
        # Validación del rango del percentil
        if not (0 <= p <= 100):
            raise ValueError("El percentil debe estar entre 0 y 100.")

        # Elimina valores nulos y ordena los datos
        datos_ordenados = sorted(self.datos.dropna())
        n = self.contar_datos()

        # Si no hay datos válidos, retorna NaN
        if n == 0:
            return float('nan')

        # Posición teórica dentro del conjunto ordenado
        k = (p / 100) * (n - 1)

        # Índices inferior (f) y superior (c)
        f = int(np.floor(k))
        c = int(np.ceil(k))

        # Si ambos índices son iguales, el percentil coincide con ese valor
        if f == c:
            return datos_ordenados[f]
        
        # Interpolación lineal entre los valores vecinos
        return datos_ordenados[f] + (k - f) * (datos_ordenados[c] - datos_ordenados[f])

# -----------------------------------------------------------
# Distribución 
#------------------------------------------------------------
    
    def normal(self, x):
        """
        Calcula el valor de la función de densidad de la distribución normal 
        para un valor específico de x.
        Parámetros:
            x (float): Valor para el cual se evalúa la densidad.
        """
        mu = self.media()
        sigma = self.desviacion_estandar()

        # Validación para evitar división por cero
        if sigma == 0:
            return 0.0

        # Fórmula de la distribución normal
        coeficiente = 1 / (sigma * math.sqrt(2 * math.pi))
        exponente = math.exp(-0.5 * ((x - mu) / sigma) ** 2)
        return coeficiente * exponente


    def normal_estandar(self, z):
        """
        Calcula el valor de la función de densidad de la distribución normal estándar 
        (media = 0, desviación estándar = 1).    
        Parámetros:
            z (float): Valor de la variable estandarizada.
        """
        coeficiente = 1 / math.sqrt(2 * math.pi)
        exponente = math.exp(-0.5 * z ** 2)
        return coeficiente * exponente
    
    def z_score(self, x):

        """
        Calcula el puntaje Z (valor estandarizado) para un valor dado de x.

        El puntaje Z indica cuántas desviaciones estándar se encuentra un valor 
        respecto a la media de la distribución.
        Parámetros:
            x (float): Valor del dato que se desea estandarizar.
        """
        mu = self.media()
        sigma = self.desviacion_estandar()

        # Evita división por cero si todos los valores son iguales
        if sigma == 0:
            raise ValueError("No se puede calcular el puntaje Z: la desviación estándar es cero.")

        return (x - mu) / sigma

#---------------------------------------------------------------
# Resumen general
#---------------------------------------------------------------

    def resumen_estadistico(self):
        """
        Genera un resumen estadístico general con las principales medidas descriptivas.
        
        Retorna:
            dict: Diccionario con medidas como media, mediana, moda, varianza, 
            desviación estándar, rango y coeficiente de variación.
        """
        # Verifica que existan datos
        if not self.datos or self.contar_datos() == 0:
            raise ValueError("No se puede generar un resumen estadístico: no hay datos disponibles.")

        return {
            "Cantidad de datos (n)": self.contar_datos(),
            "Media": round(self.media(), 2),
            "Mediana": round(self.mediana(), 2),
            "Moda": self.moda(),
            "Varianza": round(self.varianza(), 2),
            "Desviación estándar": round(self.desviacion_estandar(), 2),
            "Rango": round(self.rango(), 2),
            "Coeficiente de variación (%)": round(self.coeficiente_variacion(), 2)
        }

