function draw_map(data, container, key, value) {
    var center = new google.maps.LatLng(48.8534100, 2.3488000);

    var options = {
      'zoom': 2,
      'center': center,
      'mapTypeId': google.maps.MapTypeId.ROADMAP
    };
    var geocoder = new google.maps.Geocoder();
    var map = new google.maps.Map(document.getElementById(container), options);

    function place_mark(i) {
            geocoder.geocode({ 'address': key(data[i])}, function(results, status) {
                if ( status == google.maps.GeocoderStatus.OK ) {
                    var latLng = results[0].geometry.location;
                    var mark = new google.maps.Marker({
                        position: latLng,
                        map: map,
                        icon: 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld='+value(data[i])+'|FF0000|000000'
                    });
                } else console.log(status + " when " + key(data[i]));
            });
        };
        //var markercount = data.length
        function doPlaceMark(i) {
            setTimeout(function() { place_mark(i); }, 1000*i);
        }
        for (var i=0; i < data.length; i++) {
                doPlaceMark(i);
        }

    /*
    var markercount = 5
    for (var i=0; i < 5; i++) {
        var deferred = new $.Deferred();
        geocoder.geocode( { 'address': value(data[i])}, function(results, status) {
            if ( status == google.maps.GeocoderStatus.OK ) {
                var latLng = results[0].geometry.location;
                var mark = new google.maps.Marker({'position': latLng});
                markers.push(mark);
            }
            markercount--
            if (markercount == 0) var mc = new MarkerClusterer(map, markers);
        });
    }*/
}