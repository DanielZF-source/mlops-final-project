import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(data_path, model_path):
    # 1. Cargar datos procesados
    df = pd.read_csv(data_path)
    
    # 2. Separar características (X) y objetivo (y)
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    
    # 3. División de datos (80% entrenamiento, 20% prueba)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # 4. Entrenamiento del modelo
    print("Entrenando el modelo Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 5. Evaluación rápida
    y_pred = model.predict(X_test)
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))
    
    # 6. Serialización (Guardar el modelo)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"\nModelo serializado y guardado en: {model_path}")

if __name__ == "__main__":
    TRAINING_DATA = "data/training/churn_processed.csv"
    MODEL_OUTPUT = "models/churn_model.pkl"
    
    train_model(TRAINING_DATA, MODEL_OUTPUT)