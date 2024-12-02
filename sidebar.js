// Initialize the sidebar
function initSidebar(map_object) {
    // Create and initialize the sidebar (hidden initially)
    var sidebar = document.getElementById("sidebar");
    sidebar.style.display = 'none';  // Initially hide the sidebar

    // Create a container to store markers
    var markers = [];

    // Function to add a marker and store it with its details
    function addMarker(lat, lon, location_name, details) {
        var marker = L.marker([lat, lon]).addTo(map_object);
        marker.location_name = location_name;  // Add location name to the marker
        marker.details = details;              // Add location details (optional)
        
        marker.on('click', function() {
            // When a marker is clicked, show the sidebar and populate it
            sidebar.style.display = 'block';  // Show the sidebar
            sidebar.innerHTML = `
                <h3>${marker.location_name}</h3>
                <p>${marker.details}</p>
                <img src="${marker.details.image}" alt="Image" style="width:100%; height:auto;"/>
            `; // Insert details into the sidebar
        });
    }

    // Return the function to add markers
    return addMarker;
}

// Initialize the sidebar and markers
window.onload = function() {
    initSidebar(window.map_object);  // Assuming map_object is initialized from Python
};
