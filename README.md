# 🧮 Proyecto: Análisis Estadístico de Datos Cualitativos y Cuantitativos

## 📘 Descripción General
Este proyecto implementa un sistema en **Python** para el análisis estadístico de datos **cualitativos** y **cuantitativos**, aplicando los principios de la **Programación Orientada a Objetos (POO)**.  
El programa permite leer archivos CSV, seleccionar variables y generar automáticamente medidas estadísticas y tablas de frecuencia.  
Su diseño modular facilita el uso de clases reutilizables y promueve la claridad del código mediante la aplicación de conceptos como **herencia**, **encapsulamiento** y **polimorfismo**.  

## 🧠 Objetivos del Proyecto
Aplicar los fundamentos de la Programación Orientada a Objetos (POO) en Python.

Implementar clases reutilizables para análisis estadístico (cualitativo y cuantitativo).

Automatizar el cálculo y la generación de:

📊 Medidas de tendencia central (Media, Mediana, Moda).

📈 Medidas de dispersión (Desviación estándar).

🔢 Cuartiles/Percentiles para datos cuantitativos.

📋 Tablas de frecuencia y porcentajes para datos cualitativos.

  
  
## ✨ Características Principales
- **Carga de Datos Flexible:** Maneja archivos **.csv** con separadores **;** o **,** y codificación ***latin -1***.
- **Estadística Descriptiva:** 
  -  Cálculo de medidas de tendencia central** (Media, Mediana, Moda)** y    dispersión **(Varianza, Desviación Estándar)**

- **Análisis Gráfico:**
	- Generación automática de Histogramas y Gráficos de Barras.

- **Inferencia Estadística:**
	- Soporte para Intervalos de Confianza y las pruebas de hipótesis más comunes.
---
## 📋 Uso e Instalación
#### **Requisitos**
Este proyecto requiere las siguientes librerías de Python. Se recomienda usar un entorno virtual.

`pip install pandas numpy matplotlib scipy`  
---
Organizar la salida de resultados en directorios dedicados (tablas y graficos).


🧮 Proyecto: Análisis Estadístico de Datos Cualitativos y Cuantitativos
📘 Descripción General
Este proyecto implementa un sistema en Python para el análisis estadístico de datos cualitativos y cuantitativos, aplicando los principios de la Programación Orientada a Objetos (POO).
El programa permite leer archivos CSV, seleccionar variables y generar automáticamente medidas estadísticas y tablas de frecuencia, guardando los resultados en archivos CSV y gráficos PNG dentro de carpetas dedicadas (tablas/ y graficos/).

Su diseño modular facilita el uso de clases reutilizables y promueve la claridad del código mediante la aplicación rigurosa de conceptos de POO como:

Herencia: Uso de una clase base (DatosBase) para compartir la lógica de carga de archivos.

Encapsulamiento: Manejo interno y seguro de los datos (self.datos, self.df) dentro de cada clase.

Polimorfismo: Métodos específicos de cálculo (calcular_frecuencias, calcular_resumen) implementados de manera diferente en las clases hijas.

🧠 Objetivos del Proyecto
Aplicar los fundamentos de la Programación Orientada a Objetos (POO) en Python.

Implementar clases reutilizables para análisis estadístico (cualitativo y cuantitativo).

Automatizar el cálculo y la generación de:

📊 Medidas de tendencia central (Media, Mediana, Moda).

📈 Medidas de dispersión (Desviación estándar).

🔢 Cuartiles/Percentiles para datos cuantitativos.

📋 Tablas de frecuencia y porcentajes para datos cualitativos.

Organizar la salida de resultados en directorios dedicados (tablas y graficos).

🏗️ Estructura del Proyecto

nombre_de_tu_carpeta/
├── estadistica_lib/
│   ├── base.py                 # Clase Padre (DatosBase): Maneja la carga de CSV.
│   ├── cualitativos.py         # Clase Hija (DatosCualitativos): Métodos para Moda, Frecuencias y Gráficos de Barras.
│   ├── cuantitativos.py        # Clase Hija (DatosCuantitativos): Métodos para Media, Desviación Estándar y Histogramas.
│   ├── prueba.py               # Script principal de ejecución y demostración.
│   └── __init__.py             # Inicializa el directorio como un paquete Python.
├── datasets/
│   └── Alumnos Matriculados...csv  # Archivo de datos de entrada.
├── tablas/                     # Directorio de salida: Aquí se guardan los archivos CSV de resumen.
├── graficos/                   # Directorio de salida: Aquí se guardan los archivos PNG de los gráficos.
└── requirements.txt            # Archivo que lista las dependencias del proyecto (pandas, matplotlib).
