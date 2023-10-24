import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np


def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)


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


def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))


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


df = pd.read_csv("P2ConsumoAgua2019.csv")
df_mean = df.groupby(['bimestre', 'indice_des'])['consumo_total'].mean().reset_index()

label_to_number = {label: i for i, label in enumerate(df_mean['indice_des'].unique())}
number_to_label = {i: label for i, label in enumerate(df_mean['indice_des'].unique())}

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

# Minería de Datos
# Brian Esquivel
# 1930115
