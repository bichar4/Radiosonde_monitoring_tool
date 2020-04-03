var map;

function initialize(){
    map = L.map('map').setView([55.61121, 12.99351], 10);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18,
        id: 'mapbox/satellite-v9',
    }).addTo(map);

    var marker = L.marker(map.getCenter()).addTo(map);
    marker.bindPopup("Hello World!").openPopup();
    new QWebChannel(qt.webChannelTransport, function (channel) {
        window.MainWindow = channel.objects.MainWindow;
        if(typeof MainWindow != 'undefined') {
            var onMapMove = function() { MainWindow.onMapMove(map.getCenter().lat, map.getCenter().lng) };
            var test = function(){MainWindow.ontest("bichar")}
            map.on('move', onMapMove);
            map.on('click',test);
            onMapMove();
            test()
        }
    });
}