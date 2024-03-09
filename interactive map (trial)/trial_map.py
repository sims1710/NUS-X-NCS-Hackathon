import folium

# Create a map centered around Singapore
map_sg = folium.Map(location=[1.3521, 103.8198], zoom_start=11)

# Add markers with custom icons and popups
folium.Marker(
    location=[1.3521, 103.8198],
    popup='Merlion Park',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(map_sg)

folium.Marker(
    location=[1.2895, 103.8500],
    popup='Gardens by the Bay',
    icon=folium.Icon(color='green', icon='leaf')
).add_to(map_sg)

# Draw a polygon to outline Marina Bay Sands
marina_bay_sands_coords = [
    [1.2839, 103.8605],
    [1.2821, 103.8584],
    [1.2832, 103.8574],
    [1.2850, 103.8596]
]
folium.Polygon(locations=marina_bay_sands_coords, color='red', fill=True, fill_color='red').add_to(map_sg)

# Add layer control
folium.LayerControl().add_to(map_sg)

# Save the map
map_sg.save('cool_singapore_map.html')

