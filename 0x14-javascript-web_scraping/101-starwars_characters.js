#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function helpRequest (array, a) {
  if (a === array.length) {
    return;
  }
  req(array[a], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).name);
    helpRequest(array, a + 1);
  });
}

req(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const ch = JSON.parse(body).characters;
  helpRequest(ch, 0);
});
