var map = L.map('map').setView([37.8, -96], 4);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    id: "mapbox/light-v9",
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

L.geoJson(statesData).addTo(map);

var count = 0

var sample_data;
d3.selectAll("#selState_in").on("change", updateStateIN);
var state_value
var state_name

function updateStateIN (){
    var dropdownMenu = d3.select("#selState_in");
    state_name = dropdownMenu.property("value");
    
    
    // if (count > 0 ) {
    // map.removeTo(info);}
    // count = count + 1

    d3.json("/api/test/"+ state_name).then(
        function(data){

            function getColor(c) {
                return c > 80500 ? '#800026' :
                    c > 69000  ? '#BD0026' :
                    c > 57500  ? '#E31A1C' :
                    c > 46000  ? '#FC4E2A' :
                    c > 34500  ? '#FD8D3C' :
                    c > 23000  ? '#FEB24C' :
                    c > 1  ? '#FED976' :
                    c = 0 ? 'FFF':
                                '#23F459';
                                // '#FFEDA0';
            }

            function style(feature) {
                state_value = feature.properties.inflow;
            
                return{
                    fillColor: getColor(state_value),
                    weight: 2,
                    opacity: 1,
                    color: 'white',
                    dashArray: '3',
                    fillOpacity: 1
            
                };
                
            }
            L.geoJson(data, {style: style}).addTo(map);

            function highlightFeature(e) {
                var layer = e.target;
            
                layer.setStyle({
                    weight: 5,
                    color: '#666',
                    dashArray: '',
                    fillOpacity: 0.7
                })
                info.update(layer.feature.properties);
            };

            var info = L.control();

                info.onAdd = function (map) {
                    d3.select("div.info").remove();
                    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
                    this.update();
                    return this._div;
                };
                function resetHighlight(e) {
                    geojson.resetStyle(e.target);
                    info.update();    
                };
                var geojson;

                function zoomToFeature(e) {
                    map.fitBounds(e.target.getBounds());
                };
                function onEachFeature(feature, layer) {
                    layer.on({
                        mouseover: highlightFeature,
                        mouseout: resetHighlight,
                        click: zoomToFeature
                    });
                }
                
                geojson = L.geoJson(data, {
                    style: style,
                    onEachFeature: onEachFeature
                }).addTo(map);

                // method that we will use to update the control based on feature properties passed
                info.update = function (props) {
                    this._div.innerHTML = '<h4> State Inflow Total <br>' + state_name + '</h4>' +  (props ?
                        '<b></b><br />' + props.outflow + '  people move out of </b> ' + props.name 
                        : 'Hover over a state');
                };

                info.addTo(map);
                    });
        };   
    
d3.selectAll("#selState_out").on("change", updateStateOUT);
// d3.selectAll("#selState_out").on("change", stateSort);
function updateStateOUT (){
    var dropdownMenu = d3.select("#selState_out");
    state_name = dropdownMenu.property("value");
    //state_capital = state_name.upper()

    d3.json("/api/test/"+ state_name).then(
        
        function(data){
            

            function getColor(c) {
                return c > 80500 ? '#800026' :
                    c > 69000  ? '#BD0026' :
                    c > 57500  ? '#E31A1C' :
                    c > 46000  ? '#FC4E2A' :
                    c > 34500  ? '#FD8D3C' :
                    c > 23000  ? '#FEB24C' :
                    c > 1  ? '#FED976' :
                    c = 0 ? 'FFF':
                                '#083AF3  ';
                                // '#FFEDA0';
            }

            function style(feature) {
                state_value = feature.properties.outflow;
            
                return{
                    fillColor: getColor(state_value),
                    weight: 2,
                    opacity: 1,
                    color: 'white',
                    dashArray: '3',
                    fillOpacity: 1
                };   
            }

            L.geoJson(data, {style: style}).addTo(map);
            
            function highlightFeature(e) {
                var layer = e.target;
            
                layer.setStyle({
                    weight: 5,
                    color: '#666',
                    dashArray: '',
                    fillOpacity: 0.7
                })
                info.update(layer.feature.properties);
            };

            var info = L.control();

                info.onAdd = function (map) {
                    d3.select("div.info").remove();
                    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
                    this.update();
                    return this._div;
                };
                function resetHighlight(e) {
                    geojson.resetStyle(e.target);
                    info.update();    
                };
                var geojson;

                function zoomToFeature(e) {
                    map.fitBounds(e.target.getBounds());
                };
                function onEachFeature(feature, layer) {
                    layer.on({
                        mouseover: highlightFeature,
                        mouseout: resetHighlight,
                        click: zoomToFeature
                    });
                }
                
                geojson = L.geoJson(data, {
                    style: style,
                    onEachFeature: onEachFeature
                }).addTo(map);

                // method that we will use to update the control based on feature properties passed
                info.update = function (props) {
                    

                    this._div.innerHTML = '<h4> State Outflow Total <br>' + state_name + '</h4>' +  (props ?
                        '<b></b><br />' + props.outflow + '  people move into </b> ' + props.name 
                        : 'Hover over a state');
                };
                info.addTo(map)
                
                
                // var legend = L.control({position: 'bottomright'});

                // legend.onAdd = function (map) {

                //     var div = L.DomUtil.create('div', 'info legend'),
                //         grades = [0, 5, 10, 20, 50, 100, 200, 500, 1000],
                //         labels = [];

                //     // loop through our density intervals and generate a label with a colored square for each interval
                //     for (var i = 0; i < grades.length; i++) {
                //         div.innerHTML +=
                //             '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                //             grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
                //     }

                //     return div;
                // };

                // legend.addTo(map);
                
                    });
                
                
    ;            
};
        


            
