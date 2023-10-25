import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np


# Coloreado de los puntos para los diferentes grupos
def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)


# Genera el scatter para tanto los grupos por bimestre e índice como sólo por el índice
def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()


# Genera el scatter para los grupos por bimestre
def scatter_group_by_bim(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == {label}")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()


# Obtiene la distancia euclidiana para el algoritmo de los k vecinos
def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))


# Obtiene los k vecinos siendo 5 como valor para luego imprimir los valores en consola por cada scatter distinto
def k_nearest_neightbors(
    points: List[np.array], labels: np.array, input_data: List[np.array], k: int
):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    predicted_labels = [
        np.argmax(np.bincount([label_to_number[labels[index]] for index in point_nearest]))
        for point_nearest in points_k_nearest
    ]

    return predicted_labels


# Comienzo de la lectura del CSV y otro agrupado para obtener el primer scatter
df = pd.read_csv("P2ConsumoAgua2019.csv")
df_mean = df.groupby(['bimestre', 'indice_des'])['consumo_total'].mean().reset_index()

# Se usan en los k vecinos para que no haya problema con los labels del scatter
label_to_number = {label: i for i, label in enumerate(df_mean['indice_des'].unique())}
number_to_label = {i: label for i, label in enumerate(df_mean['indice_des'].unique())}

#Primera llamada al scatter mandando como eje x el consumo total, el y como bimestre, y los labels que sean las descripciones de los índices
scatter_group_by("scatterP7/grupos.png", df_mean, "consumo_total", "bimestre", "indice_des")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df_mean.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df_mean[['consumo_total','bimestre']].to_numpy(),
    df_mean['indice_des'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

# Igual que arriba pero con distinto dataframe usado
label_to_number = {label: i for i, label in enumerate(df['indice_des'].unique())}
number_to_label = {i: label for i, label in enumerate(df['indice_des'].unique())}

#Llamada al scatter mandando como eje x el consumo total doméstico, el y como consumo total, y los labels que sean las descripciones de los índices
scatter_group_by("scatterP7/gruposDom.png", df, "consumo_total_dom", "consumo_total", "indice_des")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['consumo_total_dom','consumo_total']].to_numpy(),
    df['indice_des'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

#Llamada al scatter mandando como eje x el consumo total no doméstico, el y como consumo total, y los labels que sean las descripciones de los índices
scatter_group_by("scatterP7/gruposNoDom.png", df, "consumo_total_no_dom", "consumo_total", "indice_des")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['consumo_total_no_dom','consumo_total']].to_numpy(),
    df['indice_des'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

#Llamada al scatter mandando como eje x el consumo total mixto, el y como consumo total, y los labels que sean las descripciones de los índices
scatter_group_by("scatterP7/gruposMixto.png", df, "consumo_total_mixto", "consumo_total", "indice_des")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['consumo_total_mixto','consumo_total']].to_numpy(),
    df['indice_des'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

# Se organiza el dataframe para que los bimestres tengan un orden ascendente
df = df.sort_values(by='bimestre', ascending=True)
# Ahora estos ayudarán para los k vecinos pero ahora la columna que será el label va a ser la de los bimestres
label_to_number = {label: i for i, label in enumerate(df['bimestre'].unique())}
number_to_label = {i: label for i, label in enumerate(df['bimestre'].unique())}

#Llamada al scatter mandando como eje x el consumo total doméstico, el y como consumo total, y los labels que sean los 3 distintos bimestres
scatter_group_by_bim("scatterP7/gruposBimDom.png", df, "consumo_total_dom", "consumo_total", "bimestre")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['consumo_total_dom', 'consumo_total']].to_numpy(),
    df['bimestre'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

#Llamada al scatter mandando como eje x el consumo total no doméstico, el y como consumo total, y los labels que sean los 3 distintos bimestres
scatter_group_by_bim("scatterP7/gruposBimNoDom.png", df, "consumo_total_no_dom", "consumo_total", "bimestre")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['consumo_total_no_dom', 'consumo_total']].to_numpy(),
    df['bimestre'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

#Llamada al scatter mandando como eje x el consumo total mixto, el y como consumo total, y los labels que sean los 3 distintos bimestres
scatter_group_by_bim("scatterP7/gruposBimMixto.png", df, "consumo_total_mixto", "consumo_total", "bimestre")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['consumo_total_mixto', 'consumo_total']].to_numpy(),
    df['bimestre'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

# Minería de Datos
# Brian Esquivel
# 1930115
