import pandas as pd
from estadistica_lib.cualitativos import DatosCualitativos

def detectar_separador(ruta):
    """Detecta automáticamente el separador del archivo CSV."""
    with open(ruta, 'r', encoding='utf-8') as f:
        primera_linea = f.readline()
        if ';' in primera_linea:
            return ';'
        elif ',' in primera_linea:
            return ','
        else:
            return ','  # por defecto

def main():
    # Ruta al archivo CSV real
    ruta = "../datasets/Alumnos Matriculados 2025-II-UNALM.csv"

    # Detectar separador automáticamente
    sep = detectar_separador(ruta)
    print(f"Separador detectado: '{sep}'")

    # Mostrar las columnas disponibles para elegir
    df = pd.read_csv(ruta, sep=sep, nrows=3)
    print("\nColumnas detectadas en el archivo:")
    for col in df.columns:
        print("-", col)

    # Pedir al usuario cuál columna cualitativa desea analizar
    columna = input("\n👉 Ingresa el nombre de la columna cualitativa que quieres analizar: ")

    try:
        analisis = DatosCualitativos(ruta, columna, separador=sep)
        resumen = analisis.resumen()

        print("\n---- RESUMEN DE DATOS CUALITATIVOS ----")
        print(f"Variable: {resumen['Variable']}")
        print(f"Tipo: {resumen['Tipo de Dato']}")
        print(f"Observaciones válidas: {resumen['Observaciones Válidas']}")
        print(f"Moda: {resumen['Moda']}")

        print("\nTabla de frecuencias:")
        tabla = pd.DataFrame(resumen["Tabla de Frecuencias"])
        print(tabla.to_string(index=False))

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

if __name__ == "__main__":
    main()
