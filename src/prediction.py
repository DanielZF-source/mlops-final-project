import requests
import pandas as pd

# 1. Cargar una fila de los datos procesados para asegurar el formato correcto
data_processed = pd.read_csv('data/training/churn_processed.csv')
# Tomamos la primera fila, eliminamos la columna objetivo 'Churn' y convertimos a diccionario
sample_row = data_processed.drop('Churn', axis=1).iloc[0].to_dict()

URL = "http://127.0.0.1:8000/predict"
payload = {"data": sample_row}

def test_prediction():
    try:
        response = requests.post(URL, json=payload)
        if response.status_code == 200:
            print("¡Predicción exitosa!")
            print(f"Resultado: {response.json()}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    test_prediction()