#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  for (let cent = 0; cent < list.length; cent++) {
    if (list[cent] === searchElement) {
      a++;
    }
  }
  return a;
};
