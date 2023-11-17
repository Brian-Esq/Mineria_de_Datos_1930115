from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


# Abre el archivo txt que se le envía en modo lectura y regresa como valor las que se consideran palabras separadas
# por un espacio
def open_file(path: str) -> str:
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)


# Se usa para pasarle el dataframe y la columna especificada, y con esto valida que primero se encuentre la columna
# Después de validarla regresa las palabras unidas en una misma cadena separadas por un espacio
def open_dataframe_column(df: pd.DataFrame, column_name: str) -> str:
    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        raise ValueError(f"La columna '{column_name}' no existe en el DataFrame.")

    # Obtener el contenido de la columna como una cadena
    content = " ".join(df[column_name].astype(str))

    return content


# Inicio de word cloud con el archivo txt
all_words = ""
frase = open_file("texto.txt")
palabras = frase.rstrip().split(" ")
# Se usa para obtener las palabras que se vayan repitiendo por cada iteración para tomar en cuenta cuáles serán las
# más grandes en el wordcloud
for arg in palabras:
    tokens = arg.split()
    all_words += " ".join(tokens) + " "
# Generación de la imagen de la nube de palabras
wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(all_words)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("textCloudP10/palabrasTXT.png")
plt.close()


# Se aplicará el mismo proceso pero ahora usando las palabras de la columna Colonia dentro del DataSet generado
# en la práctica 2
df = pd.read_csv("P2ConsumoAgua2019.csv")
palabras = open_dataframe_column(df, 'colonia')
palabras = " ".join(palabras.split())
# Se genera y guarda la nube de palabras de las colonias en el dataset
wordcloud2 = WordCloud(background_color="white", min_font_size=5).generate(palabras)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud2)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("textCloudP10/palabrasColoniaCSV.png")
plt.close()


# Se aplicará el mismo proceso pero ahora usando las palabras de la columna Alcaldía dentro del DataSet generado
# en la práctica 2
palabras2 = open_dataframe_column(df, 'alcaldia')
palabras2 = " ".join(palabras2.split())
wordcloud3 = WordCloud(background_color="white", min_font_size=5).generate(palabras2)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud3)
plt.axis("off")
plt.tight_layout(pad=0)
# Se genera y guarda la nube de palabras de las alcaldías en el dataset
plt.savefig("textCloudP10/palabrasAlcaldiaCSV.png")
plt.close()


# Minería de Datos
# Brian Esquivel
# 1930115
