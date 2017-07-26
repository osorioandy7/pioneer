
  // This example requires the Places library. Include the libraries=places
  // parameter when you first load the API. For example:
  // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

  var map;
  var infowindow;

  function initMap() {
    var pyrmont = {lat: 33.9950762, lng: -118.4784572};

    map = new google.maps.Map(document.getElementById('map'), {
      center: pyrmont,
      zoom: 10
    });
    var card = document.getElementById('pac-card');
   var input = document.getElementById('pac-input');
   var types = document.getElementById('type-selector');
   var strictBounds = document.getElementById('strict-bounds-selector');

   map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

   var autocomplete = new google.maps.places.Autocomplete(input);

   // Bind the map's bounds (viewport) property to the autocomplete object,
   // so that the autocomplete requests use the current map bounds for the
   // bounds option in the request.
   autocomplete.bindTo('bounds', map);

   var infowindow = new google.maps.InfoWindow();
   var infowindowContent = document.getElementById('infowindow-content');
   infowindow.setContent(infowindowContent);
   var marker = new google.maps.Marker({
     map: map,
     anchorPoint: new google.maps.Point(0, -29)
   });

   autocomplete.addListener('place_changed', function() {
     infowindow.close();
     marker.setVisible(false);
     var place = autocomplete.getPlace();
     if (!place.geometry) {
       // User entered the name of a Place that was not suggested and
       // pressed the Enter key, or the Place Details request failed.
       window.alert("No details available for input: '" + place.name + "'");
       return;
     }

     // If the place has a geometry, then present it on a map.
     if (place.geometry.viewport) {
       map.fitBounds(place.geometry.viewport);


     } else {
       map.setCenter(place.geometry.location);
       map.setZoom(17);  // Why 17? Because it looks good.

     }
     marker.setPosition(place.geometry.location);
     marker.setVisible(true);


     var address = '';
     if (place.address_components) {
       address = [
         (place.address_components[0] && place.address_components[0].short_name || ''),
         (place.address_components[1] && place.address_components[1].short_name || ''),
         (place.address_components[2] && place.address_components[2].short_name || '')
       ].join(' ');
     }

     infowindowContent.children['place-icon'].src = place.icon;
     infowindowContent.children['place-name'].textContent = place.name;
     infowindowContent.children['place-address'].textContent = address;
     infowindow.open(map, marker);
     var service = new google.maps.places.PlacesService(map);
     service.nearbySearch({
       location: {lat:map.getCenter().lat(),lng: map.getCenter().lng()},
       radius: 100000,
       type: ['university']
     }, callback);

     //.latLng.lat()
   });

   // Sets a listener on a radio button to change the filter type on Places
   // Autocomplete.
   function setupClickListener(id, types) {
     var radioButton = document.getElementById(id);
     radioButton.addEventListener('click', function() {
       autocomplete.setTypes(types);
     });
   }

   setupClickListener('changetype-all', []);
   setupClickListener('changetype-address', ['address']);
   setupClickListener('changetype-establishment', ['establishment']);
   setupClickListener('changetype-geocode', ['geocode']);

   document.getElementById('use-strict-bounds')
       .addEventListener('click', function() {
         console.log('Checkbox clicked! New state=' + this.checked);
         autocomplete.setOptions({strictBounds: this.checked});
       });
       function callback(results, status) {
         if (status === google.maps.places.PlacesServiceStatus.OK) {
           for (var i = 0; i < results.length; i++) {
             createMarker(results[i]);
           }
         }
       }

       function createMarker(place) {
         var placeLoc = place.geometry.location;
         var marker = new google.maps.Marker({
           map: map,
           position: place.geometry.location

         });

         google.maps.event.addListener(marker, 'click', function() {
           infowindow.setContent(place.name);
           infowindow.open(map, this);
         });
}

  infoWindow = new google.maps.InfoWindow;

         // Try HTML5 geolocation.
         if (navigator.geolocation) {
           navigator.geolocation.getCurrentPosition(function(position) {
             var pos = {
               lat: position.coords.latitude,
               lng: position.coords.longitude
             };

             infoWindow.setPosition(pos);
             infoWindow.setContent('Location found.');
             infoWindow.open(map);
             map.setCenter(pos);
             infowindow = new google.maps.InfoWindow();
             var service = new google.maps.places.PlacesService(map);
             service.nearbySearch({
               location: {lat: position.coords.latitude, lng: position.coords.longitude},
               radius: 100000,
               type: ['university']
             }, callback);

           }, function() {
             handleLocationError(true, infoWindow, map.getCenter());
           });
         } else {
           // Browser doesn't support Geolocation
           handleLocationError(false, infoWindow, map.getCenter());
         }


       function handleLocationError(browserHasGeolocation, infoWindow, pos) {
         infoWindow.setPosition(pos);
         infoWindow.setContent(browserHasGeolocation ?
                               'Error: The Geolocation service failed.' :
                               'Error: Your browser doesn\'t support geolocation.');
         infoWindow.open(map);
       }

  }
//MIT Lat/Long: 42.360091,-71.0963487
