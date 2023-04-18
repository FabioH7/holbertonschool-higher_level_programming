#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const filepath = process.argv[2];

fs.writeFile(filepath, process.argv[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
