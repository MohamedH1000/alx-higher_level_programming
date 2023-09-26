#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req.get(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
