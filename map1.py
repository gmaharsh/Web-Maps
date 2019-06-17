import folium
map = folium.Map(location = [50, 100], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location= [50.2, 99],popup="Hello", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")