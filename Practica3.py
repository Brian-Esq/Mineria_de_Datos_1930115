import pandas as pd
from tabulate import tabulate
from typing import Tuple, List

#Lectura del CSV para guardarlo en un dataframe
csvFile = "P2ConsumoAgua2019.csv"
df = pd.read_csv(csvFile)

#Se obtienen los datos estadísticos para la columna del consumo total por bimestre y se guarda en un CSV
df_total = df.groupby(["bimestre", "indice_des"]).agg({'consumo_total': ['sum', 'count', 'mean', 'min', 'max']})
df_total = df_total.reset_index()
newCSVFile = "csvP3/ConsumoBimestralTotal.csv"
df_total.to_csv(newCSVFile, index=False)

#Se obtienen los datos estadísticos para la columna del consumo mixto (doméstico y no doméstico) por bimestre y se guarda en un CSV
df_mixto = df.groupby(["bimestre", "indice_des"]).agg({'consumo_total_mixto': ['sum', 'count', 'mean', 'min', 'max']})
df_mixto = df_mixto.reset_index()
newCSVFile = "csvP3/ConsumoBimestralTotalMixto.csv"
df_mixto.to_csv(newCSVFile, index=False)

#Se obtienen los datos estadísticos para la columna del consumo total doméstico por bimestre y se guarda en un CSV
df_domestico = df.groupby(["bimestre", "indice_des"]).agg({'consumo_total_dom': ['sum', 'count', 'mean', 'min', 'max']})
df_domestico = df_domestico.reset_index()
newCSVFile = "csvP3/ConsumoBimestralTotalDomestico.csv"
df_domestico.to_csv(newCSVFile, index=False)

#Se obtienen los datos estadísticos para la columna del consumo total no doméstico por bimestre y se guarda en un CSV
df_noDomestico = df.groupby(["bimestre", "indice_des"]).agg({'consumo_total_no_dom': ['sum', 'count', 'mean', 'min', 'max']})
df_noDomestico = df_noDomestico.reset_index()
newCSVFile = "csvP3/ConsumoBimestralTotalNoDom.csv"
df_noDomestico.to_csv(newCSVFile, index=False)

# Minería de Datos
# Brian Esquivel
# 1930115
