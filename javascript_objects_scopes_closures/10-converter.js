#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (number) {
    return parseInt(number + '', 10)
      .toString(base);
  };
};
