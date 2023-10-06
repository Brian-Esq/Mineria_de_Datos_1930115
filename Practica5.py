import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Análisis de las varianzas sobre el consumo entre los índices alto, medio, bajo y popular por...

# Consumo total en los 3 bimestres
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSum = df.groupby(["indice_des", "bimestre"])[["consumo_total"]].sum()
df_BimSum.reset_index(inplace=True)
df_BimSum.set_index("indice_des", inplace=True)
df_BimSum.reset_index(inplace=True)
df_Anova = df_BimSum.rename(columns={"consumo_total" : "ConsumoTotal"}).drop(['bimestre'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotal ~ indice_des", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total de los 4 índices de colonia distintos")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total de los 4 índices de colonia distintos")

# Consumo mixto en los 3 bimestres
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSumMix = df.groupby(["indice_des", "bimestre"])[["consumo_total_mixto"]].sum()
df_BimSumMix.reset_index(inplace=True)
df_BimSumMix.set_index("indice_des", inplace=True)
df_BimSumMix.reset_index(inplace=True)
df_Anova = df_BimSumMix.rename(columns={"consumo_total_mixto" : "ConsumoTotalMixto"}).drop(['bimestre'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotalMixto ~ indice_des", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total mixto de los 4 índices de colonia distintos")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total mixto de los 4 índices de colonia distintos")


# Consumo doméstico en los 3 bimestres
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSumDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_dom"]].sum()
df_BimSumDom.reset_index(inplace=True)
df_BimSumDom.set_index("indice_des", inplace=True)
df_BimSumDom.reset_index(inplace=True)
df_Anova = df_BimSumDom.rename(columns={"consumo_total_dom" : "ConsumoTotalDomestico"}).drop(['bimestre'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotalDomestico ~ indice_des", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total domestico de los 4 índices de colonia distintos")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total domestico de los 4 índices de colonia distintos")


# Consumo no doméstico en los 3 bimestres
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimSumNoDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_no_dom"]].sum()
df_BimSumNoDom.reset_index(inplace=True)
df_BimSumNoDom.set_index("indice_des", inplace=True)
df_BimSumNoDom.reset_index(inplace=True)
df_Anova = df_BimSumNoDom.rename(columns={"consumo_total_no_dom" : "ConsumoTotalNoDomestico"}).drop(['bimestre'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotalNoDomestico ~ indice_des", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total no domestico de los 4 índices de colonia distintos")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total no domestico de los 4 índices de colonia distintos")


# Análisis de las varianzas sobre el consumo entre los 3 bimestres registrados...

# Por consumo total
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTot = df.groupby(["indice_des", "bimestre"])[["consumo_total"]].sum()
df_BimTot.reset_index(inplace=True)
df_BimTot.set_index("bimestre", inplace=True)
df_BimTot.reset_index(inplace=True)
df_Anova = df_BimTot.rename(columns={"consumo_total" : "ConsumoTotal"}).drop(['indice_des'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotal ~ bimestre", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total por bimestre")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total por bimestre")

# Por consumo mixto
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimMix = df.groupby(["indice_des", "bimestre"])[["consumo_total_mixto"]].sum()
df_BimMix.reset_index(inplace=True)
df_BimMix.set_index("bimestre", inplace=True)
df_BimMix.reset_index(inplace=True)
df_Anova = df_BimMix.rename(columns={"consumo_total_mixto" : "ConsumoTotalMixto"}).drop(['indice_des'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotalMixto ~ bimestre", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total mixto por bimestre")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total mixto por bimestre")

# Por consumo doméstico
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_dom"]].sum()
df_BimDom.reset_index(inplace=True)
df_BimDom.set_index("bimestre", inplace=True)
df_BimDom.reset_index(inplace=True)
df_Anova = df_BimDom.rename(columns={"consumo_total_dom" : "ConsumoTotalDomestico"}).drop(['indice_des'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotalDomestico ~ bimestre", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total domestico por bimestre")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total domestico por bimestre")

# Por consumo no doméstico
print("\n\n")
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimNoDom = df.groupby(["indice_des", "bimestre"])[["consumo_total_no_dom"]].sum()
df_BimNoDom.reset_index(inplace=True)
df_BimNoDom.set_index("bimestre", inplace=True)
df_BimNoDom.reset_index(inplace=True)
df_Anova = df_BimNoDom.rename(columns={"consumo_total_no_dom" : "ConsumoTotalNoDomestico"}).drop(['indice_des'], axis=1)
print(df_Anova.head())

model = ols("ConsumoTotalNoDomestico ~ bimestre", data=df_Anova).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencias para el consumo total no domestico por bimestre")
    print(anovaDF)
else:
    print("No hay diferencias para el consumo total no domestico por bimestre")

# Minería de Datos
# Brian Esquivel
# 1930115
