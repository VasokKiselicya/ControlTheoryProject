function init_map() {
    var myOptions = {
        zoom: 16,
        center: new google.maps.LatLng(48.2929567, 25.92979230000003),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('gmap_canvas'), myOptions);
    marker = new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(48.2929567, 25.92979230000003)
    });
    infowindow = new google.maps.InfoWindow({content: '<b>м. Чернівці <br> вул. Університетська 28<b>'});
    google.maps.event.addListener(marker, 'click', function () {
        infowindow.open(map, marker);
    });
    infowindow.open(map, marker);
}

google.maps.event.addDomListener(window, 'load', init_map);