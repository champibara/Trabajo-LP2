# estadistica_lib/prueba.py (Código completo y final)

# Se importa la funcionalidad de manejo de archivos.
import os
# Se importa la librería para manejo de datos.
import pandas as pd
# Se importan las Clases Hijas para la ejecución de la lógica.
from estadistica_lib.cualitativos import DatosCualitativos
from estadistica_lib.cuantitativos import DatosCuantitativos
from estadistica_lib.inferencia import InferenciaEstadistica # <-- Importación clave

# 1. CONSTANTES DE CONFIGURACIÓN Y RUTA
RUTA_DATASET = 'datasets/Alumnos Matriculados 2025-II-UNALM.csv'
DIR_TABLAS = 'tablas'
DIR_GRAFICOS = 'graficos'

def crear_directorios():
    """Se verifica y se crean los directorios de salida (tablas y graficos) si no existen."""
    for d in [DIR_TABLAS, DIR_GRAFICOS]:
        os.makedirs(d, exist_ok=True)
    print("Directorios de salida verificados/creados.")


def main():
    
    crear_directorios() 
    print("--- TAREA LP2: Estadística con POO ---")
    
    # ----------------------------------------------------
    # 1. PRUEBA CON DATOS CUALITATIVOS
    columna_cualitativa = 'FACULTAD' 

    try:
        datos_cual = DatosCualitativos(RUTA_DATASET, columna_cualitativa)
        datos_cual.mostrar_info()
        
        datos_cual.guardar_tabla_frecuencias("tabla_frecuencias_cualitativas.csv")
        datos_cual.generar_y_guardar_grafico("grafico_barras_cualitativas.png")
        
        moda = datos_cual.calcular_moda()
        print(f"\nModa(s) de {columna_cualitativa}: {moda}")

    except Exception as e:
        print(f"\n[ERROR al procesar Cualitativos]: {e}")

    # ----------------------------------------------------
    # 2. PRUEBA CON DATOS CUANTITATIVOS
    columna_cuantitativa = 'NRO_MATRICULADOS' 

    try:
        datos_cuant = DatosCuantitativos(RUTA_DATASET, columna_cuantitativa)
        datos_cuant.mostrar_info()
        
        datos_cuant.guardar_resumen_estadistico("resumen_cuantitativo.csv")
        datos_cuant.generar_y_guardar_histograma("histograma_cuantitativo.png")
        
        resumen = datos_cuant.calcular_resumen()
        print("\nResumen Estadístico Cuantitativo:")
        for k, v in resumen.items():
            print(f"- {k}: {v}")
            
    except Exception as e:
        print(f"\n[ERROR al procesar Cuantitativos]: {e}")
        
    # ----------------------------------------------------
    # 3. PRUEBA CON DATOS INFERENCIALES
    # ----------------------------------------------------
    columna_inferencia = 'NRO_MATRICULADOS'
    # NOTA: Usamos los valores calculados de la muestra para la prueba Z, solo para demostrar el código.
    media_hipotetica = 57.77
    desv_conocida = 105.68     
    
    try:
        # Se crea el objeto de inferencia (Hereda de Cuantitativos)
        datos_inf = InferenciaEstadistica(RUTA_DATASET, columna_inferencia)
        
        # --- 3.1 INTERVALO DE CONFIANZA ---
        ic = datos_inf.intervalo_confianza_media(nivel_confianza=0.90)
        print("\n--- Intervalo de Confianza (90%) para la Media (μ) ---")
        print(f"IC: [{ic['Limite_Inferior']} ; {ic['Limite_Superior']}]")

        # --- 3.2 PRUEBA Z UNIMUESTRA ---
        prueba_z = datos_inf.prueba_z_media_poblacional(media_hipotetica, desv_conocida)
        print("\n--- Prueba Z Unimuestra ---")
        print(f"Estadístico Z: {prueba_z['Z_Estadístico']} | P-Valor: {prueba_z['P_Valor']}")
        print(f"Conclusión: {prueba_z['Conclusion']}")
        
    except Exception as e:
        print(f"\n[ERROR al procesar Inferencia]: {e}")
    

    print("\n--- Tarea completada exitosamente ---")


if __name__ == '__main__':
    # Se ejecuta la función principal del programa.
    main()
