var apiKey = API_KEY;

const url = "http://127.0.0.1:5000/api/v1.0/data";

// Fetch the JSON data and console log it
d3.json(url).then(function(data) {
  console.log(data);
});

// Promise Pending
const dataPromise = d3.json(url);
console.log("Data Promise: ", dataPromise);