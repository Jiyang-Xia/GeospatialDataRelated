import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def Clean(poi_file, clean_poi_data):
    df = pd.read_csv(poi_file, encoding='latin-1', sep='|')
    df.head()
    #Read columns of POI dataset
    pcolu = df.columns
    print(pcolu)
    #Read categories of POI dataset
    pcate = df.CATEGORY.value_counts()
    print(pcate)
    #Check latitude and longitude range
    print('LON(max)', df.LON.max())
    print('LON(min)', df.LON.min())
    print('LAT(max)', df.LAT.max())
    print('LAT(min)', df.LAT.min())
    # creat a filter
    filtered_data = df[
        (df['LON'] >= 2.2362174096139995) & (df['LON'] <= 2.4485807005813456) &
        (df['LAT'] >= 48.798812226180445) & (df['LAT'] <= 48.92286904929176)]
    filtered_data.to_csv(clean_poi_data, index=False)

if __name__ == "__main__":
    poi_file = "your_input_poi.csv"
    clean_poi_data = "output_clean_poi.csv"

    Clean(poi_file, clean_poi_data)
    