import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import pandas as pd

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
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)


# Regresión lineal para el consumo total de agua por alcaldía y bimestre registrada con un código
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_mean = df.groupby(['alcaldia','bimestre'])['consumo_total'].mean().reset_index()
df_mean['codCol'] = [1,2,3,4,5,6,7,8,9,10,
                     11,12,13,14,15,16,17,18,19,20,
                     21,22,23,24,25,26,27,28,29,30,
                     31,32,33,34,35,36,37,38,39,40,
                     41,42,43,44,45,46,47,48]

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
plt.savefig("LinearRegressionP6/RegresionPorAlcaldiaBimestre.png")
plt.tight_layout()
plt.close()
print(df_mean)  # Revisar esta impresión en consola para ver qué código pertenece a qué alcaldía en qué bimestre
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)


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
# Coeficiente de correlación Spearman
predicciones2 = model.predict(sm.add_constant(X2))
spearman2, p_valor2 = spearmanr(predicciones2, Y2)
print("Coeficiente de correlación de Spearman:", spearman2)
print("Valor p:", p_valor2)
# Coeficiente de correlación Pearson
coeficiente_pearson2, p_value2 = pearsonr(predicciones2, Y2)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson2)
print("Valor p:", p_value2)


# Regresión para la relación entre el consumo total y el consumo doméstico
df = df.dropna()
X = sm.add_constant(df['consumo_total_dom'])
Y = df['consumo_total']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

# Configuración del plot
plt.figure(figsize=(10, 6))
plt.scatter(df['consumo_total_dom'], df['consumo_total'], label='Consumo Domestico')
plt.plot(df['consumo_total_dom'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Consumo Doméstico')
plt.ylabel('Consumo Total')
plt.title('Regresion lineal: Consumo total a la que aporta el consumo domestico')
plt.legend()
plt.savefig("LinearRegressionP6/RegresionDomestica.png")
plt.tight_layout()
plt.close()
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)


# Regresión para la relación entre el consumo total y el consumo no doméstico
X = sm.add_constant(df['consumo_total_no_dom'])
Y = df['consumo_total']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

# Configuración del plot
plt.figure(figsize=(10, 6))
plt.scatter(df['consumo_total_no_dom'], df['consumo_total'], label='Consumo No Domestico')
plt.plot(df['consumo_total_no_dom'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Consumo No Doméstico')
plt.ylabel('Consumo Total')
plt.title('Regresion lineal: Consumo total a la que aporta el consumo no domestico')
plt.legend()
plt.savefig("LinearRegressionP6/RegresionNoDomestica.png")
plt.tight_layout()
plt.close()
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)


# Regresión para la relación entre el consumo total y el consumo mixto
X = sm.add_constant(df['consumo_total_mixto'])
Y = df['consumo_total']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

# Configuración del plot
plt.figure(figsize=(10, 6))
plt.scatter(df['consumo_total_mixto'], df['consumo_total'], label='Consumo Mixto')
plt.plot(df['consumo_total_mixto'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Consumo Mixto')
plt.ylabel('Consumo Total')
plt.title('Regresion lineal: Consumo total a la que aporta el consumo mixto')
plt.legend()
plt.savefig("LinearRegressionP6/RegresionMixta.png")
plt.tight_layout()
plt.close()
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)

# Minería de Datos
# Brian Esquivel
# 1930115
