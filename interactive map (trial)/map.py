import folium
import pandas as pd

# Load MRT station data
mrt_data = pd.read_csv('mrt_stations.csv')  # Assuming you have a CSV file containing MRT station data

# Create a map centered around Singapore
map_sg = folium.Map(location=[1.3521, 103.8198], zoom_start=11)

# Add markers for MRT stations
for index, row in mrt_data.iterrows():
    popup_content = f"<b>{row['STN_NAME']}</b>"
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_content,
        icon=folium.Icon(color='white', icon='train')
    ).add_to(map_sg)

# Add markers with weather details (assuming you have implemented the function from the previous example)

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
map_sg.save('cool_singapore_map_with_mrt.html')

