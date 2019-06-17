import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat= list(data["LAT"])
lon= list(data["LON"])
elev = list(data["ELEV"])


def color_pro(elev):
    if(elev < 1500):
        return 'green'
    elif(1500 <= elev < 2200):
        return 'blue'
    else:
        return 'red'


map = folium.Map(location = [38, -100], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")


for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el) + "m", radius = 6, fill_color = color_pro(el), color= 'grey', fill_opacity= 0.7))

fg.add_child(folium.GeoJson(data = (open('world.json', 'r', encoding= "UTF-8-sig").read())))


map.add_child(fg)
map.save("Map1.html")