import pandas as pd
import geopandas as gpd
from shapely.wkt import loads

def Csv2Geojson(csv_file):
    df = pd.read_csv(csv_file, encoding="latin-1")
    # choose and change columns to convert and take care the one contains geo information, e.g., 'geometry' or 'centroid'

    gdf = gpd.GeoDataFrame({
    'ID': df['column_id'],
    'type_name': df['column_link_type_name'],
    'link_type': df['column_link_type'],
    'geometry': df['geometry'].apply(loads)})
    gdf.to_file(output_geojson_path, driver='GeoJSON')

if __name__ == "__main__":
    csv_file = "your_input.csv"
    output_geojson_path = "your_output.geojson"

    Csv2Geojson(csv_file)
    print(f"Conversion from CSV to GeoJSON is complete. GeoJSON file saved to {output_geojson_path}")