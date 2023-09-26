#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
let ndfilms = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const films = JSON.parse(body).results;
  for (const a of films) {
    const characters = a.characters;
    if (characters.find((c) => c.endsWith('/18/'))) {
      ndfilms += 1;
    }
  }
  console.log(ndfilms);
});
