import pandas as pd
from haversine import haversine
from .models import Parkings, Free
import requests

parkings = Parkings.objects.all()
locations = []
latitude = []
longitude = []

for parking in parkings:
    locations.append(parking.location)
    latitude.append(parking.latitude)
    longitude.append(parking.longitude)
    
#takes parameter of user's location
def getParkings():
    df = pd.DataFrame({ 
        'location': locations,
        'latitude': latitude,
        'longitude': longitude
    })

    #user's location
    users_lat_lon = (40.94, -74.05)
    # users_lat_lon = (lat, long)
    df['distance'] = df.apply(lambda row: haversine((row['latitude'], row['longitude']), users_lat_lon), axis=1)
    filtered_df = df[df['distance'] <= 1000]
    return filtered_df

#this function takes in parkings within the radius
#then gets the images of the respective locations
def find_free_parkings(parkings):
    
    locations = parkings.location
    latitude = parkings.latitude
    longitude = parkings.longitude
    free = []
    
    #Fetch from parking lots
    for location in locations:
        p_kings = Parkings.objects.get(location = location)
        from_db = Free.objects.get(parking = p_kings.id)
        
        if from_db.free > 0:
            free.append(from_db)
    
    #get the locations with free parking
    for location, lat, long in zip(locations, latitude, longitude):
        #Getting images for each cordinate
        url = 'https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom=20&size=400x400&maptype=satellite&key=AIzaSyCfPrg8MdEm0nXZkWNQqSFSUgXxVyUVYFc'
        img = requests.get(url)
        # image = img.content
        #feeding the free location to be returned by the function
        free.append(location)
        # print(img.content)
    
    #passing the images to the machine learning model
    
    return free