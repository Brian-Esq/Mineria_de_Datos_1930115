import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate
from statsmodels.stats.outliers_influence import summary_table
from typing import Tuple, Dict
import numpy as np


def transform_variable(df: pd.DataFrame, x:str) -> pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])


def linear_reg(df: pd.DataFrame, x:str, y: str) -> Dict[str, float]:
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())
    coef = model.params
    m = coef.values[1]
    b = coef.values[0]
    r_2_t_df = pd.DataFrame(model.summary().tables[0])
    r2 = r_2_t_df.values[0][3]
    r2_adj = r_2_t_df.values[1][3]
    band_table = model.summary().tables[1][1]
    lb = str(band_table[5])
    lb = float(lb)
    hb = str(band_table[6])
    hb = float(hb)
    return {'m': m , 'b': b, 'r2': r2, 'r2_adj': r2_adj , 'low_band': lb, 'hi_band': hb}


def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[m * x + b for _, x in fixed_x.items()], color='green')
    plt.fill_between(df[x], [m * x + low_band for _, x in fixed_x.items()], [m * x + hi_band for _, x in fixed_x.items()], alpha=0.5, color='red')


df = pd.read_csv("P2ConsumoAgua2019.csv")
eliminar = ['fecha_referencia','bimestre','consumo_total_mixto','consumo_total_no_dom','indice_des','colonia','alcaldia','latitud','longitud']
df_con_tot_dom = df.drop(eliminar, axis=1)
df_con_tot_dom.reset_index(inplace=True)
df_con_tot_dom = df_con_tot_dom.dropna()
lin = linear_reg(df_con_tot_dom, "consumo_total_dom", "consumo_total")
plt_lr(df=df_con_tot_dom, x="consumo_total_dom", y="consumo_total", **lin)
plt.xticks(rotation=90)
plt.savefig('forecastP9/primerScatter.png')
plt.close()

df_mean = df.groupby(['alcaldia','bimestre'])['consumo_total'].mean().reset_index()
df_mean['codCol'] = [1,2,3,4,5,6,7,8,9,10,
                     11,12,13,14,15,16,17,18,19,20,
                     21,22,23,24,25,26,27,28,29,30,
                     31,32,33,34,35,36,37,38,39,40,
                     41,42,43,44,45,46,47,48]

lin = linear_reg(df_mean, "codCol", "consumo_total")
plt_lr(df=df_mean, x="codCol", y="consumo_total", **lin)
plt.xticks(rotation=90)
plt.savefig('forecastP9/segundoScatter.png')
plt.close()
