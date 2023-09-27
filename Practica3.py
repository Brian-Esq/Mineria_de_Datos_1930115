import pandas as pd
from tabulate import tabulate
from typing import Tuple, List

csvFile = "P2ConsumoAgua2019.csv"
df = pd.read_csv(csvFile)

df_bim = df.groupby(["bimestre", "indice_des"]).agg({'consumo_total': ['sum', 'count', 'mean', 'min', 'max']})
df_bim = df_bim.reset_index()

newCSVFile = "csv/ConsumoBimestral.csv"
df_bim.to_csv(newCSVFile, index=False)
