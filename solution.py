import pandas as pd
import requests
import json

# Cargar datos demográficos
url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
data_demographics = pd.read_csv(url, sep=';')
print("Datos demográficos cargados.")

# Limpiar datos demográficos
data_demographics = data_demographics.drop(columns=['Race', 'Count', 'Number of Veterans'])
data_demographics = data_demographics.drop_duplicates()
print("Datos demográficos limpiados.")

# Configuración de la API de calidad del aire
airquality_api_url = "https://api-ninjas.com/api/airquality"
api_key = 'CQhmSEih8ZBbWDNdOu9bHg==gPy6Xgx6eAZM8x5r'

air_quality_dimensions = pd.DataFrame(columns=['City', 'Air_Quality_Concentration'])

# Iterar sobre las filas de los datos demográficos
for index, row in data_demographics.iterrows():
    city = row['City']

city = ''
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)

# Eliminar filas con valores nulos en la tabla de dimensiones
air_quality_dimensions = air_quality_dimensions.dropna()
print("Datos de calidad del aire obtenidos y tabla de dimensiones creada.")

# Mostrar la tabla de dimensiones de calidad del aire
print("Tabla de Dimensiones - Calidad del Aire:")
print(air_quality_dimensions)

# Guardar la tabla de dimensiones en un archivo CSV
air_quality_dimensions.to_csv("tabla_calidad_aire_dimensiones.csv", index=False)
print("Tabla de dimensiones guardada en archivo CSV.")
