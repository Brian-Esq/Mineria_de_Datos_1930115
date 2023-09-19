import pandas as pd

# Lectura de un archivo con un dataframe
csvFile = "ConsumoAgua2019.csv"
df = pd.read_csv(csvFile)

# Eliminación de las columnas que no se quieren en el CSV
deleteColumns = ["anio", "consumo_prom_dom", "consumo_prom_mixto", "consumo_prom", "consumo_prom_no_dom"]
df = df.drop(columns=deleteColumns)

# Guardado del nuevo archivo CSV con las columnas eliminadas
newCSVFile = "P2ConsumoAgua2019.csv"
df.to_csv(newCSVFile, index=False)

# Se dejaron solamente las columnas que son consideradas útiles
# Minería de Datos
# Brian Esquivel
# 1930115
