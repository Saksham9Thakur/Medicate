var directionsService;
var directionsDisplay;
function initMap() {
  window.directionsService = new google.maps.DirectionsService;
  window.directionsDisplay = new google.maps.DirectionsRenderer;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 6,
    center: {lat: 30.7333, lng: 76.7794}
  });
  directionsDisplay.setMap(map);
console.log(window.directionsDisplay);
}

function calculateAndDisplayRoute(a) {
  var waypts = [];
/*  var checkboxArray = document.getElementById('waypoints');
  for (var i = 0; i < checkboxArray.length; i++) {
    if (checkboxArray.options[i].selected) {
      waypts.push({
        location: checkboxArray[i].value,
        stopover: true
      });
    }
  }*/
/*console.log(window.directionsService);
console.log(window.directionsDisplay);*/
/* var a = document.getElementById('saa').innerHTML;
 console.log(a);*/
 window.directionsService.route({
    origin:"Indira Gandhi Medical Hospital Shimla",
    destination: "Jaypee University Of Information Technology",
    waypoints: waypts,
    optimizeWaypoints: true,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      window.directionsDisplay.setDirections(response)
      var route = response.routes[0];
      var summaryPanel = document.getElementById('directions-panel');
      summaryPanel.innerHTML = '';
      // For each route, display summary information.
      for (var i = 0; i < route.legs.length; i++) {
        var routeSegment = i + 1;
        summaryPanel.innerHTML += '<b>Route Segment: ' + routeSegment +
            '</b><br>';
    /*    summaryPanel.innerHTML += route.legs[i].start_address + ' to ';
        summaryPanel.innerHTML += route.legs[i].end_address + '<br>';
        summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
      console.log(route.legs[i]);*/
      }
    } else 
    {
      window.alert('Directions request failed due to ' + status);
    }
  });
}