import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Se obtienen los boxplot por bimestre e índice de desarrollo de la colonia para la media de...

#Consumo total de agua en el primer semestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTotal = df.groupby(["indice_des", "bimestre"])[["consumo_total"]].mean()
df_BimTotal.boxplot(by = 'indice_des', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("graficasP4/boxplotConsumoTotalMean.png")
plt.close()

#Consumo de agua en inmuebles domésticos y no domésticos en el primer semestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTotalMix = df.groupby(["indice_des", "bimestre"])[["consumo_total_mixto"]].mean()
df_BimTotalMix.boxplot(by = 'indice_des', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("graficasP4/boxplotConsumoTotalMixtoMean.png")
plt.close()

#Consumo de agua doméstico en el primer semestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTotalDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_dom"]].mean()
df_BimTotalDom.boxplot(by = 'indice_des', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("graficasP4/boxplotConsumoTotalDomMean.png")
plt.close()

#Consumo de agua no doméstico en el primer semestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTotalNoDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_no_dom"]].mean()
df_BimTotalNoDom.boxplot(by = 'indice_des', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("graficasP4/boxplotConsumoTotalNoDomMean.png")
plt.close()

#Se obtienen los plot por índice de desarrollo de la colonia para la sumatoria de de...

#Consumo total de agua en el primer, segundo y tercer bimestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSum = df.groupby(["indice_des", "bimestre"])[["consumo_total"]].sum()
df_BimSum.reset_index(inplace=True)
df_BimSum.set_index("indice_des", inplace=True)
for bim in set(df_BimSum['bimestre']):
    df_BimSum[df_BimSum['bimestre'] == bim].plot(y = "consumo_total")
    plt.savefig(f"graficasP4/plotConsumoBim{bim}.png")
    plt.close()

#Consumo de agua en inmuebles domésticos y no domésticos en el primer, segundo y tercer bimestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSumMixto = df.groupby(["indice_des", "bimestre"])[["consumo_total_mixto"]].sum()
df_BimSumMixto.reset_index(inplace=True)
df_BimSumMixto.set_index("indice_des", inplace=True)
for bim in set(df_BimSumMixto['bimestre']):
    df_BimSumMixto[df_BimSumMixto['bimestre'] == bim].plot(y = "consumo_total_mixto")
    plt.savefig(f"graficasP4/plotConsumoMixtoBim{bim}.png")
    plt.close()

#Consumo de agua en inmuebles domésticos en el primer, segundo y tercer bimestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSumDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_dom"]].sum()
df_BimSumDom.reset_index(inplace=True)
df_BimSumDom.set_index("indice_des", inplace=True)
for bim in set(df_BimSumDom['bimestre']):
    df_BimSumDom[df_BimSumDom['bimestre'] == bim].plot(y = "consumo_total_dom")
    plt.savefig(f"graficasP4/plotConsumoDomBim{bim}.png")
    plt.close()

#Consumo de agua en inmuebles no domésticos en el primer, segundo y tercer bimestre de 2019
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSumNoDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_no_dom"]].sum()
df_BimSumNoDom.reset_index(inplace=True)
df_BimSumNoDom.set_index("indice_des", inplace=True)
for bim in set(df_BimSumNoDom['bimestre']):
    df_BimSumNoDom[df_BimSumNoDom['bimestre'] == bim].plot(y = "consumo_total_no_dom")
    plt.savefig(f"graficasP4/plotConsumoNoDomBim{bim}.png")
    plt.close()

#Consumo total de agua en el primer semestre de 2019 por alcaldia
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTotal = df.groupby(["alcaldia", "bimestre"])[["consumo_total"]].mean()
df_BimTotal.boxplot(by = 'alcaldia', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("graficasP4/boxplotConsumoTotalMeanAlcaldia.png")
plt.close()

# Minería de Datos
# Brian Esquivel
# 1930115
