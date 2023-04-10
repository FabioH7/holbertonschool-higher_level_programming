#!/usr/bin/node
const process = require('process');
const myArray = [];
let myNum = 0;
for (const number of process.argv) {
  if (myNum >= 2) {
    myArray.push(parseInt(number));
  }
  myNum++;
}
const final = myArray.filter((x) => {
  return x < Math.max(...myArray);
});
if (final.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...final));
}
