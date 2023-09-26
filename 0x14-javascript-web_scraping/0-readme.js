#!/usr/bin/node
const file = require('fs');

file.readFile(process.argv[2], 'utf8', function (error, details) {
  if (error) {
    console.log(error);
  }
  console.log(details);
});
