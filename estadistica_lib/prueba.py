# estadistica_lib/prueba.py

# Se importa la funcionalidad de manejo de archivos.
import os 
# Se importa la librería para manejo de datos.
import pandas as pd
# Se importan las Clases Hijas para la ejecución de la lógica.
from estadistica_lib.cualitativos import DatosCualitativos
from estadistica_lib.cuantitativos import DatosCuantitativos

# 1. CONSTANTES DE CONFIGURACIÓN Y RUTA
# Se corrige la ruta para la ejecución como módulo (desde la raíz del proyecto).
RUTA_DATASET = 'datasets/Alumnos Matriculados 2025-II-UNALM.csv'
DIR_TABLAS = 'tablas'
DIR_GRAFICOS = 'graficos'

def crear_directorios():
    """Se verifica y se crean los directorios de salida (tablas y graficos) si no existen."""
    # Se utiliza os.makedirs con exist_ok=True para crear directorios sin error si ya existen.
    for d in [DIR_TABLAS, DIR_GRAFICOS]:
        os.makedirs(d, exist_ok=True)
    print("Directorios de salida verificados/creados.")


def main():
    
    # Se llama a la función para asegurar que las carpetas de salida existan.
    crear_directorios() 
    print("--- TAREA LP2: Estadística con POO ---")
    
    # ----------------------------------------------------
    # 1. PRUEBA CON DATOS CUALITATIVOS
    # Se usa 'FACULTAD' como la columna de datos cualitativos (CORREGIDO)
    columna_cualitativa = 'FACULTAD' 

    try:
        # Se crea el objeto de la clase hija (Herencia).
        datos_cual = DatosCualitativos(RUTA_DATASET, columna_cualitativa)
        datos_cual.mostrar_info()
        
        # Se llama a los métodos para guardar resultados.
        datos_cual.guardar_tabla_frecuencias("tabla_frecuencias_cualitativas.csv")
        datos_cual.generar_y_guardar_grafico("grafico_barras_cualitativas.png")
        
        # Se muestra la moda por consola.
        moda = datos_cual.calcular_moda()
        print(f"\nModa(s) de {columna_cualitativa}: {moda}")

    except Exception as e:
        print(f"\n[ERROR al procesar Cualitativos]: {e}")

    # ----------------------------------------------------
    # 2. PRUEBA CON DATOS CUANTITATIVOS
    # Se usa 'NRO_MATRICULADOS' como la columna de datos cuantitativos (CORREGIDO)
    columna_cuantitativa = 'NRO_MATRICULADOS' 

    try:
        # Se crea el objeto de la clase hija (Herencia).
        datos_cuant = DatosCuantitativos(RUTA_DATASET, columna_cuantitativa)
        datos_cuant.mostrar_info()
        
        # Se llama a los métodos para guardar resultados.
        datos_cuant.guardar_resumen_estadistico("resumen_cuantitativo.csv")
        datos_cuant.generar_y_guardar_histograma("histograma_cuantitativo.png")
        
        # Se muestra el resumen por consola.
        resumen = datos_cuant.calcular_resumen()
        print("\nResumen Estadístico Cuantitativo:")
        for k, v in resumen.items():
            print(f"- {k}: {v}")
            
    except Exception as e:
        print(f"\n[ERROR al procesar Cuantitativos]: {e}")
        
    print("\n--- Tarea completada exitosamente ---")


if __name__ == '__main__':
    # Se ejecuta la función principal del programa.
    main()
