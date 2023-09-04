import requests     # Hace las peticiones
from bs4 import BeautifulSoup   # Ayuda a analizar el contenido de la página HTML
import re   # Ayuda a trabajar con las expresiones regulares
import urllib.request   # Sirve para descargar el csv
url = "https://datos.cdmx.gob.mx/tl/dataset/consumo-agua"   # Link de donde se obtuvieron los datos

# Guarda el link de la forma para poder guardar el archivo csv
link_csv = BeautifulSoup(requests.get(url).text, 'html.parser').find('a', href=re.compile(r'\.csv$')).get('href')

# Descarga el archivo del link establecido con el nombre indicado y el tipo de archivo que es
urllib.request.urlretrieve(link_csv, "ConsumoAgua2019.csv")

# Minería de Datos
# Brian Esquivel
# 1930115