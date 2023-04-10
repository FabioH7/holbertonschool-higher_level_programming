#!/usr/bin/node
const process = require('process');
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  let myNum = 0;
  while (myNum < process.argv[2]) {
    console.log('C is fun');
    myNum++;
  }
}
