function initMap() {

	var belmont = {
		info: '<strong>Chipotle on Belmont</strong><br>\
					1025 W Belmont Ave<br> Chicago, IL 60657<br>\
					<a href="https://goo.gl/maps/PHfsWTvgKa92">Get Directions</a>',
		lat: 30.7645,
		long: 76.7764 
	};


	var locations = [
    
      [belmont.info, belmont.lat, belmont.long, 0]
    ];

	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 13,
		center: new google.maps.LatLng(31.1033,77.1722),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	var image = 'images.png';
var beachMarker = new google.maps.Marker({
   position: {lat: 31.1033, lng:77.1722},
   map: map,
   icon: image
 });


	
	var bounds = new google.maps.LatLngBounds();
	var infowindow = new google.maps.InfoWindow(); 
	var marker, i;

	for (i = 0; i < locations.length; i++) {
		marker = new google.maps.Marker({
			position: new google.maps.LatLng(locations[i][1], locations[i][2]),
			map: map
		});
  bounds.extend(marker.position);
		google.maps.event.addListener(marker, 'click', (function (marker, i) {
			return function () {
				infowindow.setContent(locations[i][0]);
				infowindow.open(map, marker);
			}
		})(marker, i));
		map.fitBounds (bounds);

	/*var listener = google.maps.event.addListener(map, "idle", function () {
    map.setZoom(3);
    google.maps.event.removeListener(listener);
	});*/
}
}
