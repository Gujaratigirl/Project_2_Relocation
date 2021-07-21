var map = L.map('map').setView([37.8, -96], 4);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    id: "mapbox/light-v9",
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

L.geoJson(statesData).addTo(map);

var selected_state = d3.select("#indiana");

var sample_data;
var state_name
var state_value

d3.json("/api/statemigration/CA").then(
    function(data){
    // {   console.log(data.features[0].properties.name);
        // state_name = data.features[0].properties.name
        
        // console.log(data.features[0].properties.flows[2].inflow);
        // state_value = data.features[0].properties.flows[2].inflow;

        function getColor(c) {
            return c > 80500 ? '#800026' :
                   c > 69000  ? '#BD0026' :
                   c > 57500  ? '#E31A1C' :
                   c > 46000  ? '#FC4E2A' :
                   c > 34500  ? '#FD8D3C' :
                   c > 23000  ? '#FEB24C' :
                   c > 11000  ? '#FED976' :
                              '#FFEDA0';
        }

        function style(feature) {
            // var c = 1000;
            // state_name = data.features[0].properties.name
            // state_value = feature.properties.flows[2].inflow;
            state_value = feature.properties.inflow;
        
            return{
                fillColor: getColor(state_value),
                weight: 2,
                opacity: 1,
                color: 'white',
                dashArray: '3',
                fillOpacity: 0.7
        
            };

             
        }
        L.geoJson(data, {style: style}).addTo(map);
    })

    
    
    

