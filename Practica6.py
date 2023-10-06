import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate

# Regresión lineal para el consumo total de agua por alcaldía registrada con un código
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_mean = df.groupby('alcaldia')['consumo_total'].mean().reset_index()
df_mean['codCol'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

X = sm.add_constant(df_mean['codCol'])
Y = df_mean['consumo_total']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

# Configuración del plot
plt.figure(figsize=(10, 6))
plt.scatter(df_mean['codCol'], df_mean['consumo_total'], label='Promedios por Alcaldia')
plt.plot(df_mean['codCol'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Alcaldias por Codigo')
plt.ylabel('Promedio de Consumo Total')
plt.title('Regresion lineal: Promedio de consumo total por alcaldia para los 3 bimestres')
plt.legend()
plt.savefig("LinearRegressionP6/RegresionPorAlcaldia.png")
plt.tight_layout()
plt.close()
print(df_mean)  # Revisar esta impresión en consola para ver qué código pertenece a qué alcaldía


# Regresión lineal para el consumo total de agua por índice y bimestre clasificados por un código
df_ind = df.groupby(['bimestre', 'indice_des'])['consumo_total'].mean().reset_index()
df_ind['codigoIndiceBimestre'] = [1,2,3,4,5,6,7,8,9,10,11,12]

X2 = sm.add_constant(df_ind['codigoIndiceBimestre'])
Y2 = df_ind['consumo_total']
model = sm.OLS(Y2, X2).fit()
print(model.summary())

# Configuración del plot
plt.figure(figsize=(10, 6))
plt.scatter(df_ind['codigoIndiceBimestre'], df_ind['consumo_total'], label='Promedios por Indice y Bimestre')
plt.plot(df_ind['codigoIndiceBimestre'], model.predict(X2), color='red', label='Pendiente de Regresión')
plt.xlabel('Indices y Bimestres por Codigo')
plt.ylabel('Promedio de Consumo Total')
plt.title('Regresion lineal: Promedio de consumo total por indices y bimestres')
plt.legend()
plt.savefig("LinearRegressionP6/RegresionPorIndBim.png")
plt.tight_layout()
plt.close()
print(df_ind)   # Revisar esta impresión en consola para ver qué código pertenece a qué índice en cuál bimestre

# Minería de Datos
# Brian Esquivel
# 1930115
