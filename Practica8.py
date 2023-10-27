import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np


# Algoritmo de k-means que agrupa los puntos por su "centro de masa" dependiendo de las agrupaciones
def k_means(points: List[np.array], k: int, name: str):
    dim = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, dim))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    plt.savefig(f"kmeanScatterP8/{name}.png")
    plt.close()
    return mean


# Comienzo de la lectura del CSV y otro agrupado para obtener el primer scatter
df = pd.read_csv("P2ConsumoAgua2019.csv")
# Dataframe que agrupa por bimestre y la descripción del índice
df_mean = df.groupby(['bimestre', 'indice_des'])['consumo_total'].mean().reset_index()
df_mean = df_mean.drop('indice_des', axis=1)
list_t = [
    (np.array(tuples[0:2]), tuples[1])
    for tuples in df_mean.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
# LLamada a la función para obtener las agrupaciones por centros de masa del df_mean
kn = k_means(
    points,
    4,
    'kmeansMean'
)
print(kn)


# Se usa el dataframe donde se va a dejar únicamente el consumo total total y el consumo total, pero los agrupa a todos como si fueran un sólo monto
eliminar = ['fecha_referencia','bimestre','consumo_total_mixto','consumo_total_no_dom','indice_des','colonia','alcaldia','latitud','longitud']
df_con_tot_dom = df.drop(eliminar, axis=1)
list_t = [
    (np.array(tuples[0:2]), tuples[1])
    for tuples in df_con_tot_dom.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
kn = k_means(
    points,
    4,
    'kmeansConTotDom'
)
print(kn)

