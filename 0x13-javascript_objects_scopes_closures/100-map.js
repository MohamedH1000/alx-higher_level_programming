#!/usr/bin/node

const listOrig = require('./100-data').list;
console.log(listOrig);
const listMap = listOrig.map (function (a, index) {
  return (a * index);
});
console.log(listMap);
