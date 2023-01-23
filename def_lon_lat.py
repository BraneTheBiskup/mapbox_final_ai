from mapbox import StaticStyle
from os import mkdir, listdir

#Definicija koja prima dvije vanjske koordinete grada (BBOX), te pomoću njih napravi grid malih "pločica" gdje su koordinate njihovo središte 
#def that takes two coordinates of a city(bbox), and makes a grid of smaller bboxes where the first coordiate of a city is a center coordinate of a first smaller bbox

def lon_lat(lon_min, lat_min, lon_max, lat_max):
    latitude = []
    longitude = []

    lon = lon_max
    lat = lat_max
    
    #calculated by hand, depends on the zoom level (15,25)
    lon_inc = 0.0184
    lat_inc = 0.0128000
    
    while lon > lon_min:
        longitude.append(lon)
        lon = lon - lon_inc

    while lat > lat_min:
        latitude.append(lat)
        lat = lat - lat_inc


    return [(round(lon, 4), round(lat, 4)) for lon in longitude for lat in latitude]
    
#Def koji prima koordinate dobivene iz "def lon_lat" te za svaku radi sliku dimenzije 1024*1024*3 na zoom-u od 15.25(najveći zum koji pokazuje građevine). Te slike sprema u folder gradovi/"city_name"
#def takes coordinates from "def lon_lat", and from each downloads a static image with dimensions 1024x1024x3, and saves them in folder gradovi/"city_name"
def get_static_images(longitude, latitude, city_name):

    service = StaticStyle(access_token="pk.eyJ1Ijoi.......................api key here...................................")
    
    if((f'{city_name.lower()}' in listdir('./gradovi') and f'{longitude}_{latitude}.png' not in listdir(f'./gradovi/{city_name.lower()}')) or f'{city_name.lower()}' not in listdir('./gradovi')):
        response = service.image(username="branimirb", 
                            style_id="write name of your layer of defoult layer",
                            lon=longitude, 
                            lat=latitude, 
                            zoom=15.25, 
                            width=1024, 
                            height=1024)

        response.headers['Content-Type']
        if city_name.lower() not in listdir('./gradovi'):
            mkdir(f'gradovi/{city_name.lower()}')

        with open(f'./gradovi/{city_name.lower()}/{longitude}_{latitude}.png', 'wb') as output:_ = output.write(response.content)


