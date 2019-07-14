let myLong, myLat;
let map;
let zoom = 17;

const countries = ['america', 'us', 'u.s.', 'afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina', 'burundi', 'cambodia', 'cameroon', 'canada', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo', 'croatia', 'cuba', 'cyprus', 'denmark', 'djibouti', 'dominica', 'ecuador', 'egypt', 'eritrea', 'estonia', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea', 'guyana', 'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'namibia', 'nauru', 'nepal', 'netherlands', 'nicaragua', 'niger', 'nigeria', 'norway', 'oman', 'pakistan', 'palau', 'panama', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'rwanda', 'samoa', 'senegal', 'serbia', 'seychelles', 'singapore', 'slovakia', 'slovenia', 'somalia', 'spain', 'sudan', 'suriname', 'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'togo', 'tonga', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'uruguay', 'uzbekistan', 'vanuatu', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe'];
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

  $('#marker').show();
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

// user has submitted a country they wish to view
function submit() {
  let input = $('#input').val();
  input = input.toLowerCase();
  if (countries.includes(input)) {
    alert(input + ' is valid!');
  } else {
    alert(input + ' is invalid!');
  }
  $('#input').val('');
}

getLocation();
