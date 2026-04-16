# LAB-01 — Programación Básica en Python

Laboratorio introductorio de programación en Python orientado al análisis descriptivo de datos. El objetivo es resolver 12 preguntas de procesamiento y análisis de un conjunto de datos en formato CSV utilizando **únicamente las funciones y librerías nativas de Python** (sin pandas, numpy ni scipy).

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Requisitos previos](#requisitos-previos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación y configuración](#instalación-y-configuración)
- [Uso](#uso)
- [Ejecución de pruebas](#ejecución-de-pruebas)
- [Restricciones](#restricciones)

---

## Descripción

Este laboratorio contiene 12 ejercicios (`pregunta_01.py` – `pregunta_12.py`) en los que se debe leer y procesar el archivo `files/input/data.csv` para obtener resultados específicos de análisis. Cada ejercicio expone una función llamada `pregunta_0X()` que devuelve el resultado esperado.

El conjunto de datos incluye registros con campos como categoría, valor numérico, fecha y pares clave-valor adicionales, sobre los que se aplican operaciones de conteo, agrupación, filtrado y agregación.

---

## Requisitos previos

- Python 3.9 o superior
- `pip` (gestor de paquetes de Python)

---

## Estructura del proyecto

```
LAB-01-programacion-basica-en-python/
├── files/
│   └── input/
│       └── data.csv          # Conjunto de datos de entrada
├── homework/
│   ├── __init__.py
│   ├── notebook.ipynb        # Notebook de exploración
│   ├── pregunta_01.py        # Ejercicio 1
│   ├── ...
│   └── pregunta_12.py        # Ejercicio 12
├── tests/
│   ├── __init__.py
│   └── test_homework.py      # Pruebas automáticas (autograding)
├── requirements.txt          # Dependencias del proyecto
├── setup.py
├── setup.sh                  # Script de configuración para MacOS/Linux
└── setup.bat                 # Script de configuración para Windows
```

---

## Instalación y configuración

### MacOS y Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

### Windows

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup
```

---

## Uso

Cada archivo `homework/pregunta_0X.py` contiene una función `pregunta_0X()`. Para ejecutar una pregunta de forma individual:

```bash
python homework/pregunta_01.py
```

También puede explorar y desarrollar las soluciones de forma interactiva desde el notebook:

```bash
jupyter notebook homework/notebook.ipynb
```

---

## Ejecución de pruebas

Las pruebas verifican automáticamente la corrección de todas las soluciones:

```bash
pytest
```

---

## Restricciones

- **No** se permite el uso de `pandas`, `numpy` ni `scipy`.
- Solo se pueden utilizar las funciones y librerías estándar de Python.