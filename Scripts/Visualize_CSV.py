import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

def CSVread(csv_file):
    df = pd.read_csv(csv_file, encoding='latin-1')
    # 清理包含非数字值的列，例如 'column_to_convert'
    column_to_convert = 'LAT'  # 替换为实际的列名
    df[column_to_convert] = pd.to_numeric(df[column_to_convert], errors='coerce')
    # 创建 GeoDataFrame
    geometry = [Point(lon, lat) for lon, lat in zip(df['LON'], df['LAT'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    # 返回 GeoDataFrame
    return gdf

def visualize_geojson(geojson_file):
    # 可视化
    geojson_file.plot()
    plt.show()

if __name__ == "__main__":
    csv_file = "filtered_Paris_poi.csv"

    # 调用函数
    geojson_file = CSVread(csv_file)
    # 可视化 GeoDataFrame
    visualize_geojson(geojson_file)
