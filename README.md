# MLOps Final Project: Predicción de Churn de Clientes (Telecom)

**Estudiante:** Zavala Figueroa Daniel Angel  
**Email:** daniel.zavala.f@uni.pe  
**Curso:** Introducción a MLOps - Ciclo III - Grupo 02  

---

## 1. Descripción del Proyecto
Este repositorio contiene la implementación completa del ciclo de vida de Machine Learning (ML Lifecycle) para la predicción de fuga de clientes (Churn). El proyecto aplica principios de **MLOps** para garantizar la reproducibilidad, modularidad y escalabilidad del modelo, desde el manejo de datos inmutables hasta el despliegue de una API de inferencia.

---

## 2. Definición del Problema (Fase A)

### Contexto
El objetivo es predecir la probabilidad de que un cliente abandone una compañía de telecomunicaciones. Identificar a estos clientes permite ejecutar estrategias de fidelización dirigidas.

### Metodología y Métricas
* **Tipo de Problema:** Clasificación Binaria.
* **Métrica Principal:** **Recall** (Minimizar los falsos negativos para asegurar que detectamos a la mayor cantidad de clientes en riesgo).
* **Dataset:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

---

## 3. Estructura del Repositorio (Fase B)
Siguiendo las mejores prácticas, el proyecto se organiza de la siguiente manera

```text
├── data/
│   ├── raw/             # Dataset original e inmutable.
│   └── training/        # Dataset procesado (churn_processed.csv).
├── experiments/         # Scripts de exploración y pruebas preliminares.
├── models/              # Modelo serializado (churn_model.pkl).
├── notebooks/           # Jupyter Notebooks con análisis visual (EDA) y gráficos.
├── reports/             # Resumen de experimentos y métricas finales.
├── resources/           # Evidencias: capturas de la API y gráficos del EDA.
├── src/                 # Código fuente modular.
│   ├── data_preparation.py  # Script de transformación de datos.
│   ├── train.py             # Script de entrenamiento y guardado del modelo.
│   ├── serving.py           # API de inferencia desarrollada con FastAPI.
│   └── prediction.py        # Script para testeo automatizado de predicciones.
└── requirements.txt     # Dependencias necesarias para el entorno.

---

## 4. Desarrollo y Experimentación (Fase C y D)

### Exploración de Datos (EDA)
Se realizaron análisis visuales y estadísticos en la carpeta `notebooks/` para identificar patrones de fuga y correlaciones clave. Estos experimentos permitieron justificar la selección de variables para el modelo final.
* **Resultados Visuales:** Los gráficos de importancia de variables y distribución de Churn se encuentran en la carpeta `resources/`.

### Entrenamiento del Modelo
Se implementó un algoritmo de **Random Forest Classifier** en `src/train.py`. Este modelo fue seleccionado por su robustez ante variables categóricas y su capacidad para manejar desbalances en el dataset.
* **Serialización:** El modelo entrenado se guarda automáticamente en `models/churn_model.pkl` para su posterior consumo.
* **Métricas Finales:** El reporte detallado de precisión, recall y F1-score se encuentra registrado en la carpeta `reports/`.

---

## 5. Despliegue e Inferencia (Fase E)

El modelo se sirve a través de una **REST API** construida con **FastAPI**, permitiendo realizar predicciones en tiempo real mediante peticiones JSON.

### Instrucciones para Ejecución:

1. **Lanzar el Servidor de Inferencia:**
   Desde la raíz del proyecto, ejecute:
   ```bash
   uvicorn src.serving:app --reload

---

## 6. Control de Versiones y Entrega (Fase F)
    Siguiendo el flujo de trabajo de MLOps

    El desarrollo se gestionó mediante ramas de características (Feature Branches).

    La entrega final se realiza a través de un Pull Request (PR) hacia la rama main.

    Se asignó al docente como Reviewer en el PR para la revisión detallada del código y la estructura del proyecto.
