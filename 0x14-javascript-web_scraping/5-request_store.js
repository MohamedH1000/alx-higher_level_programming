#!/usr/bin/node
const file = require('fs');
const req = require('request');
const url = process.argv[2];
const path = process.argv[3];

req.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  file.writeFile(path, body, error => {
    if (error) console.log(error);
  });
});
