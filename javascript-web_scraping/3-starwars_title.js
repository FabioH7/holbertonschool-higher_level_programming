#!/usr/bin/node

const process = require('process');
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(api, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  console.log(response.body['title']); // Print the response status code if a response was received
});
