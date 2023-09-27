#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  for (const c of characters) {
    req(c, function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
