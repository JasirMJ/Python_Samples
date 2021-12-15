function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
        
    } else { 
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    cl = "Latitude: " + position.coords.latitude + " Longitude: " + position.coords.longitude;
    console.log("Current loc ",cl);
}

getLocation()