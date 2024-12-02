import folium
import os

# Define the starting location (latitude, longitude)
start_location = [38.38780784603443, 27.04460799730398]  # Starting location for the map

# Read coordinates from the newcoordinates.txt file (tab-separated)
coordinates = []
with open('newcoordinates.txt', 'r') as coord_file:
    for line in coord_file:
        try:
            lat, lon = line.strip().split('\t')  # Split by tab
            lat, lon = float(lat), float(lon)
            coordinates.append((lat, lon))
        except ValueError:
            print(f"Skipping invalid coordinate line: {line.strip()}")

# Read location names from the newlocations.txt file (each location on a separate line)
location_names = []
with open('newlocations.txt', 'r') as name_file:
    for line in name_file:
        location_names.append(line.strip())  # Handle location names as-is (including commas)

# Read capacity information from the newcapacities.txt file (each row is a capacity)
capacities = []
with open('newcapacities.txt', 'r') as capacity_file:
    for line in capacity_file:
        capacities.append(line.strip())  # Assuming one capacity per row

# Read area information from the newareas.txt file (each row is an area)
areas = []
with open('newareas.txt', 'r') as area_file:
    for line in area_file:
        areas.append(line.strip())  # Assuming one area per row

# Read codenames from the newcodes.txt file (each row is a codename)
codenames = []
with open('newcodes.txt', 'r') as code_file:
    for line in code_file:
        codenames.append(line.strip())  # Assuming one codename per row

# Ensure the number of coordinates, locations, capacities, areas, codenames, and images are the same
if len(coordinates) != len(location_names) or len(coordinates) != len(capacities) or len(coordinates) != len(areas) or len(coordinates) != len(codenames):
    print("Warning: The number of coordinates, locations, capacities, areas, or codenames do not match.")
    print(f"Coordinates count: {len(coordinates)}, Location names count: {len(location_names)}, Capacity count: {len(capacities)}, Area count: {len(areas)}, Codename count: {len(codenames)}")

# Create a map centered at the desired starting location
if coordinates and location_names and capacities and areas and codenames:
    map_object = folium.Map(location=start_location, zoom_start=15)  # Center map at the updated start_location

    # Add markers with popups showing the location name, capacity, area, codename, and photo (URL)
    for i, (coord, location_name, capacity, area, codename) in enumerate(zip(coordinates, location_names, capacities, areas, codenames)):
        # Create HTML content for the popup with a URL to the image
        image_url = f"https://github.com/kutay0/balcova_emer_map/raw/main/pics/{i+1}.jpg"
        popup_content = f"""
        <div style="text-align:center;">
            <img src="{image_url}" alt="{location_name}" style="width:100%;max-width:300px;border-radius:15px;"><br>
            <strong>{location_name}</strong><br>
            {codename}<br>
            <em>Capacity:</em> {capacity}<br>
            <em>Area:</em> {area} m²
        </div>
        """
        
        # Add marker with the popup
        folium.Marker(
            location=coord,
            popup=folium.Popup(popup_content, max_width=300)  # Popup with location, codename, capacity, area, and image
        ).add_to(map_object)

    # Save the map to an HTML file
    map_object.save('newmap.html')
    print("Map has been saved as 'newmap.html'")
else:
    print("No valid data found.")
