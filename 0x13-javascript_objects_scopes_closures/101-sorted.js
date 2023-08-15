#!/usr/bin/node

const dict = require('./101-data.js').dict;

const dictNew = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (dictNew[dict[occurences]] === undefined) {
    dictNew[dict[occurences]] = [occurences];
  } else {
    dictNew[dict[occurences]].push(occurences);
  }
});
console.log(dictNew);
