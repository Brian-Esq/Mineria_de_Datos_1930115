from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


def open_file(path: str) -> str:
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)


def open_dataframe_column(df: pd.DataFrame, column_name: str) -> str:
    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        raise ValueError(f"La columna '{column_name}' no existe en el DataFrame.")

    # Obtener el contenido de la columna como una cadena
    content = " ".join(df[column_name].astype(str))

    return content


all_words = ""
frase = open_file("texto.txt")
palabras = frase.rstrip().split(" ")

Counter(" ".join(palabras).split()).most_common(10)
for arg in palabras:
    tokens = arg.split()
    all_words += " ".join(tokens) + " "

wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(all_words)

# print(all_words)
# plot the WordCloud image
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# plt.show()
plt.savefig("textCloudP10/palabrasTXT.png")
plt.close()


df = pd.read_csv("P2ConsumoAgua2019.csv")
palabras = open_dataframe_column(df, 'colonia')
palabras = " ".join(palabras.split())
wordcloud2 = WordCloud(background_color="white", min_font_size=5).generate(palabras)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud2)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig("textCloudP10/palabrasColoniaCSV.png")
plt.close()


palabras2 = open_dataframe_column(df, 'alcaldia')
palabras2 = " ".join(palabras2.split())
wordcloud3 = WordCloud(background_color="white", min_font_size=5).generate(palabras2)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud3)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig("textCloudP10/palabrasAlcaldiaCSV.png")
plt.close()
