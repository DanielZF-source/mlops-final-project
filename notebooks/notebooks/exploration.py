import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Visualización de la variable objetivo
plt.figure(figsize=(6,4))
sns.countplot(x='Churn', data=df)
plt.title('Distribución de Churn')
plt.savefig('../resources/churn_distribution.png') # Guardamos en resources como pidió
plt.show()