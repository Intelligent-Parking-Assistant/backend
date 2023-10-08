import pandas as pd
from haversine import haversine
from .models import Parkings

parkings = Parkings.objects.all()

def getParkings():
    df = pd.DataFrame({
        'location': ['Norean', 'OKC', 'New York', 'Bayonne'],
        'latitude': [35.221, 35.463, 41.112, 40.66],
        'longitude': [-97.481, -97.622, -74.1083, -74.106]
    })

    jersey_city_lat_lon = (40.94, -74.05)
    df['distance'] = df.apply(lambda row: haversine((row['latitude'], row['longitude']), jersey_city_lat_lon), axis=1)
    filtered_df = df[df['distance'] <= 1000]
    return filtered_df