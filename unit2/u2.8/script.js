let myLong, myLat;
let map;
let zoom = 15;

// ask user for permission to get their location
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

// success function for the get location function
function showPosition(position) {
  let lat = position.coords.latitude;
  let long = position.coords.longitude;

  myLong = long;
  myLat = lat;
  showMap(long, lat);
}

// show map of the long and lat coordinates
function showMap(long, lat) {
  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([long, lat]),
      zoom: zoom
    })
  });
  // add marker for my location to the map
  var marker = new ol.Overlay({
    position: ol.proj.fromLonLat([myLong, myLat]),
      positioning: 'center-center',
      element: document.getElementById('marker'),
      stopEvent: false
    });
    map.addOverlay(marker);
}

// pan map view to long and lat coordinates
function setView(long, lat) {
  map.setView(new ol.View({
    center: ol.proj.fromLonLat([long, lat]),
    zoom : zoom
  }));
}

// go back to my current location
function panHome() {
  setView(myLong, myLat);
}

getLocation();
