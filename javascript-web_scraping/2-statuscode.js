#!/usr/bin/node

const process = require('process');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
