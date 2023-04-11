#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c = 'X') {
    for (let x = 0; x < this.height; x++) {
      let line = '';
      for (let y = 0; y < this.width; y++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
