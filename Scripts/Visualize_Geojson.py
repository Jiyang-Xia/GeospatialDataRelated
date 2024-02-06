import geopandas as gpd
import matplotlib.pyplot as plt

# read GeoJSON file, put your file here
gdf = gpd.read_file('output_poi.geojson')

# visualization
gdf.plot()
plt.show()
