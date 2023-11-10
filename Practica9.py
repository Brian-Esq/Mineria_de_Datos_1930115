import numbers
from typing import Dict
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


# Función para obtebner las x númericas, donde si originalmente no son númericas, se transforman en éstas
def transform_variable(df: pd.DataFrame, x:str) -> pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])


# Función para cuando se quiere obtener la predicción por colonias específicas, mandando como parámentros su
# rango de códigos
def modif_col(df_mean: pd.DataFrame, x:str, val_inf:int, val_sup:int):
    if val_inf != 0 and val_sup != 0:
        df = df_mean.loc[(df_mean[x] >= val_inf) & (df_mean[x]<=val_sup)].reset_index()
        print(df)
        return df
    else:
        return df_mean


# Creación de la regresión lineal principal, donde se genera un modelo en base al dataframe pasado y las columnas
# definidas, y toma del summary los valores necesarios para crearlas. Incluídos el lower y higher bound para hacer
# el rango coloreado más adelante
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
    return {'m': m, 'b': b, 'r2': r2, 'r2_adj': r2_adj, 'low_band': lb, 'hi_band': hb}


# Creación del plot con sus puntos, donde se grafican todos los puntos pasados del dataframe, la regresión lineal
# y un coloreado superior e inferior que predice el comportamiento futuro de los datos
def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[m * x + b for _, x in fixed_x.items()], color='green')
    plt.fill_between(df[x], [m * x + low_band for _, x in fixed_x.items()], [m * x + hi_band for _, x in fixed_x.items()], alpha=0.5, color='red')


# Lectura del dataframe general
df = pd.read_csv("P2ConsumoAgua2019.csv")
# Se hará la predicción para el consumo total con el consumo total doméstico
eliminar = ['fecha_referencia','bimestre','consumo_total_mixto','consumo_total_no_dom','indice_des','colonia','alcaldia','latitud','longitud']
df_con_tot_dom = df.drop(eliminar, axis=1)
df_con_tot_dom.reset_index(inplace=True)
df_con_tot_dom = df_con_tot_dom.dropna()
df_con_tot_dom = df_con_tot_dom.loc[df_con_tot_dom['consumo_total'] <= 30000]
lin = linear_reg(df_con_tot_dom, "consumo_total_dom", "consumo_total")
plt_lr(df=df_con_tot_dom, x="consumo_total_dom", y="consumo_total", **lin)
plt.xticks(rotation=90)
plt.savefig('forecastP9/relConTotYDomPlotModif.png')
plt.close()


# Se hará la predicción para el consumo total por cada colonia y bimestre separadas por códigos
df_mean = df.groupby(['alcaldia','bimestre'])['consumo_total'].mean().reset_index()
df_mean['codCol'] = [1,2,3,4,5,6,7,8,9,10,
                     11,12,13,14,15,16,17,18,19,20,
                     21,22,23,24,25,26,27,28,29,30,
                     31,32,33,34,35,36,37,38,39,40,
                     41,42,43,44,45,46,47,48]
# Mandar valores de entre 1 a 3, 4 a 6, 7 a 9 hasta el 46 a 48 para el análisis específico de
# una colonia y predecir su rango de consumo en el próximo bimestre
# O mandar 0 en ambos valores integer para que se haga análisis completo de todas las colonias
df_mean= modif_col(df_mean,'codCol',0,0)
lin = linear_reg(df_mean, "codCol", "consumo_total")
plt_lr(df=df_mean, x="codCol", y="consumo_total", **lin)
plt.xticks(rotation=90)
plt.savefig('forecastP9/relConYColoniaPlot.png')
plt.close()


# Se hará la predicción para el consumo total con el consumo total no doméstico
eliminar = ['fecha_referencia','bimestre','consumo_total_mixto','consumo_total_dom','indice_des','colonia','alcaldia','latitud','longitud']
df_con_tot_no_dom = df.drop(eliminar, axis=1)
df_con_tot_no_dom.reset_index(inplace=True)
df_con_tot_no_dom = df_con_tot_no_dom.dropna()
df_con_tot_no_dom = df_con_tot_no_dom.loc[df_con_tot_no_dom['consumo_total'] <= 30000]
lin = linear_reg(df_con_tot_no_dom, "consumo_total_no_dom", "consumo_total")
plt_lr(df=df_con_tot_no_dom, x="consumo_total_no_dom", y="consumo_total", **lin)
plt.xticks(rotation=90)
plt.savefig('forecastP9/relConTotYNoDomPlotModif.png')
plt.close()


# Se hará la predicción para el consumo total con el consumo total mixto
eliminar = ['fecha_referencia','bimestre','consumo_total_no_dom','consumo_total_dom','indice_des','colonia','alcaldia','latitud','longitud']
df_con_tot_mixto = df.drop(eliminar, axis=1)
df_con_tot_mixto.reset_index(inplace=True)
df_con_tot_mixto = df_con_tot_mixto.dropna()
df_con_tot_mixto = df_con_tot_mixto.loc[df_con_tot_mixto['consumo_total'] <= 30000]
lin = linear_reg(df_con_tot_mixto, "consumo_total_mixto", "consumo_total")
plt_lr(df=df_con_tot_mixto, x="consumo_total_mixto", y="consumo_total", **lin)
plt.xticks(rotation=90)
plt.savefig('forecastP9/relConTotYMixPlotModif.png')
plt.close()

# Minería de Datos
# Brian Esquivel
# 1930115
