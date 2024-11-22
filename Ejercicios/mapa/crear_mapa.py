# pip install geopandas matplotlib pandas
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

ruta_base = "Ejercicios/mapa/SHP_ETRS89/ll_autonomicas_inspire_peninbal_etrs89/"
# Cargar un shapefile de las provincias de España
spain_provinces = gpd.read_file(ruta_base + "ll_autonomicas_inspire_peninbal_etrs89.shp")

print(spain_provinces.columns)
print(spain_provinces["NAME_BOUND"].head())  # Inspecciona los primeros valores de NAME_BOUND
print(spain_provinces["NATLEVNAME"].head())  # Inspecciona los primeros valores de NATLEVNAME
print(spain_provinces["LEGSTATUS"].head())  # Inspecciona los primeros valores de NATLEVNAME
print(spain_provinces["NATLEV"].head())  # Inspecciona los primeros valores de NATLEVNAME
print()

# Tabla de datos (Provincia / Número)
data = {
    "Provincia": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Málaga"],  # Agrega todas las provincias
    "Número": [10, 20, 15, 5, 30]
}
data_df = pd.DataFrame(data)
print(data_df)

# Unir los datos con el shapefile
spain_provinces = spain_provinces.merge(data_df, left_on="Provincia", right_on="Provincia", how="left")

# Plotear el mapa
fig, ax = plt.subplots(figsize=(10, 10))
spain_provinces.plot(ax=ax, color="lightblue", edgecolor="black")

# Añadir los números en el centro de cada provincia
for x, y, label in zip(spain_provinces.geometry.centroid.x, spain_provinces.geometry.centroid.y, spain_provinces["Número"]):
    plt.text(x, y, str(label), fontsize=8, ha="center", color="darkred")

plt.title("Mapa de España con Números por Provincia", fontsize=14)
plt.axis("off")
plt.show()
