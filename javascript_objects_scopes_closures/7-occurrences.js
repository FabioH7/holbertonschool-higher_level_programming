#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (const index of list) {
    if (index === searchElement) {
      x++;
    }
  }
  return x;
};
