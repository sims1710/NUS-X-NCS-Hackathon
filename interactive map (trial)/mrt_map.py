import folium
import pandas as pd

# Load MRT station data
mrt_data = pd.read_csv('mrt_stations.csv')  # Assuming you have a CSV file containing MRT station data

# Define MRT lines with their respective stations
lines = {
    'East West Line': ['EW1', 'EW2', 'EW3', 'EW4', 'EW5', 'EW6', 'EW7', 'EW8', 'EW9', 'EW10', 'EW11', 'EW12', 'EW13', 'EW14', 'EW15', 'EW16', 'EW17', 'EW18', 'EW19', 'EW20', 'EW21', 'EW22', 'EW23', 'EW24', 'EW25', 'EW26', 'EW27', 'EW28', 'EW29', 'EW30', 'EW31', 'EW32', 'EW33', 'CG', 'CG1', 'CG2'],
    'North South Line': ['NS1', 'NS2', 'NS3', 'NS4', 'NS5', 'NS6', 'NS7', 'NS8', 'NS9', 'NS10', 'NS11', 'NS12', 'NS13', 'NS14', 'NS15', 'NS16', 'NS17', 'NS18', 'NS19', 'NS20', 'NS21', 'NS22', 'NS23', 'NS24', 'NS25', 'NS26', 'NS27', 'NS28'],
    'North East Line': ['NE1', 'NE2', 'NE3', 'NE4', 'NE5', 'NE6', 'NE7', 'NE8', 'NE9', 'NE10', 'NE11', 'NE12', 'NE13', 'NE14', 'NE15', 'NE16', 'NE17', 'NE18'],
    'Thomson-East Coast Line' : ['TE1', 'TE2', 'TE3', 'TE4', 'TE5', 'TE6', 'TE7', 'TE8', 'TE14', 'TE11', 'TE9'],
    'Downtown Line': ['DT1', 'DT2', 'DT3', 'DT4', 'DT5', 'DT6', 'DT7', 'DT8', 'DT9', 'DT10', 'DT11', 'DT12', 'DT13', 'DT14', 'DT15', 'DT16', 'DT17', 'DT18', 'DT19', 'DT20', 'DT21', 'DT22', 'DT23', 'DT24', 'DT25', 'DT26', 'DT27', 'DT28', 'DT29', 'DT30', 'DT31', 'DT32', 'DT33', 'DT34', 'DT35'],
    'Circle Line': ['CE1', 'CE2', 'CE3', 'CE4', 'CE5', 'CE6', 'CE7', 'CE8', 'CE9', 'CE10', 'CE11', 'CE12', 'CE13', 'CE14', 'CE15', 'CE16', 'CE17', 'CE18', 'CE19', 'CE20', 'CE21', 'CE22', 'CE23', 'CE24', 'CE25', 'CE26', 'CE27', 'CE28', 'CE29'],
    'Bukit Panjang LRT': ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8', 'BP9'],
    # Add more lines and their stations as needed
}

# Create a map centered around Singapore
map_sg = folium.Map(location=[1.3521, 103.8198], zoom_start=11)

# Define colors for each line
line_colors = {
    'East West Line': '#00FF00',  # Green
    'North South Line': '#FF0000',  # Red
    'North East Line': '#800080',  # Purple
    'Thomson-East Coast Line': '#8B4513',  # Brown
    'Downtown Line': '#0000FF',  # Blue
    'Circle Line': '#FFFF00',  # Yellow
}

# Add markers for MRT stations
for index, row in mrt_data.iterrows():
    popup_content = f"<b>{row['STN_NAME']}</b>"
    icon_color = '#808080'  # Default color for stations not belonging to any specific line
    for line_name, line_stations in lines.items():
        if row['STN_NO'] in line_stations:
            icon_color = line_colors.get(line_name, '#808080')  # Use line color if found
            break
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_content,
        icon=folium.Icon(color=icon_color, icon='train')
    ).add_to(map_sg)

# Add lines for each MRT line
for line_name, line_stations in lines.items():
    line_coords = [[mrt_data.loc[mrt_data['STN_NO'] == station, 'Latitude'].values[0],
                    mrt_data.loc[mrt_data['STN_NO'] == station, 'Longitude'].values[0]]
                   for station in line_stations if station in mrt_data['STN_NO'].values]
    if line_coords:  # Check if line_coords is not empty
        line_color = line_colors.get(line_name, '#808080')  # Default to gray if color not specified
        folium.PolyLine(locations=line_coords, color=line_color, weight=5, opacity=0.7, popup=line_name).add_to(map_sg)

# Save the map
map_sg.save('singapore_mrt_map.html')


