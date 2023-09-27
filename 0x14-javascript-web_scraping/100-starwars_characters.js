#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const f = JSON.parse(body);
  const ch = f.characters;
  for (const c of ch) {
    req(c, function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
