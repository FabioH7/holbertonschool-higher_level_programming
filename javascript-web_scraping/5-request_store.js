#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');
const api = process.argv[2];
const filename = process.argv[3];
let data = '';
request(api, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  data = body;
})
fs.writeFile(filename, data, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
