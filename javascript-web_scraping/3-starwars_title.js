#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');
let data = '';

if (id === undefined) process.exit(1);

request(url, (error, response, body) => {
  if (error)
    console.log(error);
  else
    console.log(JSON.parse(body).title);
});
