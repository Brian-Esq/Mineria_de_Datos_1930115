import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv("P2ConsumoAgua2019.csv")
df_BimTotal = df.groupby(["indice_des", "bimestre"])[["consumo_total"]].mean().unstack()
df_BimTotal.plot(y = 'consumo_total', legend=False, figsize=(32,18))
plt.xticks(rotation=90)
plt.savefig("graficasP4/boxplotConsumoTotal.png")
plt.close()

