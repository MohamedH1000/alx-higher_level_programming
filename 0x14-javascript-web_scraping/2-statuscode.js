#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code: ' + response.statusCode);
});
