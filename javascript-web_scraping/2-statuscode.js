#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

if (url === undefined) process.exit(1);

request(url, (error, response, body) => {
  if (error) console.log(error);
  console.log('code: ' + response.statusCode);
});
