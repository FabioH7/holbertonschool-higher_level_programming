#!/usr/bin/node
const process = require('process');
const request = require('request');
const api = process.argv[2];

request(api, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  const films = JSON.parse(response.body); // Print the response status code if a response was received
  const filtered = films.results.filter((film) => {
    for (character of film.characters) {
      if (character.includes('18')) {
        return film
      }
    }
  });
  console.log(filtered.length);
});
