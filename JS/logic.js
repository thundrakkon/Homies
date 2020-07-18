var apiKey = API_KEY;

// var url = "http://127.0.0.1:5000/api/v1.0/data";
var url = "./Resources/city_join.json"

// Fetch the JSON data and console log it
d3.json(url).then((jsonData) => {
  console.log(jsonData)

  var city = jsonData.map(row => row.city)
  var city_sorted = city.sort();
  console.log(city_sorted)

  d3.select("#selDataset")
        .selectAll("option")
        .data(city)
        .enter().append("option")
        .classed("cities", true)
        .text(function(i) {return i;})
        .exit().remove()
})

// Promise Pending
// const dataPromise = d3.json(url);
// console.log("Data Promise: ", dataPromise);