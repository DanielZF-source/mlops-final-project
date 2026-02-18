# MLOps Introduction: Final Project
FInal work description in  the [final_project_description.md](final_project_description.md) file.

Student info:
- Full name: Zavala Figueroa Daniel Angel
- e-mail: daniel.zavala.f@uni.pe
- Grupo: III Ciclo Grupo 02



# Proyecto Final: 
**Curso:** Introducción a MLOps - UNI MDS  
## Project Name: Predicción de Churn de Clientes (Telecom)

Este repositorio contiene la implementación de un ciclo de vida de Machine Learning (ML Lifecycle) completo, desde la adquisición de datos hasta el despliegue de una API, siguiendo los estándares de MLOps.

---

## A) Definición del Problema

### Contexto
El objetivo es predecir la probabilidad de que un cliente abandone una compañía de telecomunicaciones (Churn). Retener clientes es más económico que adquirir nuevos, por lo que este modelo permite tomar acciones preventivas.

### Metodología y Métricas
* **Tipo de Problema:** Clasificación Binaria.
* **Métrica Principal:** Recall (para minimizar los falsos negativos de clientes en riesgo).
* **Dataset:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

---

## B) Estructura del Proyecto
El proyecto sigue una estructura modular para garantizar la mantenibilidad:

```text
├── data/
│   ├── raw/             # Dataset original (inmutable)
│   └── training/        # Dataset procesado para el modelo
├── models/              # Modelo serializado (.pkl)
├── notebooks/           # Experimentación inicial
├── src/
│   ├── data_preparation.py # Script de transformación
│   ├── train.py            # Script de entrenamiento
│   └── serving.py          # API de inferencia (FastAPI)
└── requirements.txt     # Dependencias del proyecto
