#!/usr/bin/node
const process = require('process');
if (!process.argv[2] || isNaN(parseInt(process.argv[2])) === true) {
  console.log('Missing size');
} else {
  for (let x = 0; x < process.argv[2]; x++) {
    let line = '';
    for (let y = 0; y < process.argv[2]; y++) {
      line += 'X';
    }
    console.log(line);
  }
}
