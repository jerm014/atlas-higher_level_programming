#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let count = 0;

if (url === undefined) process.exit(1);

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    data.filter(df => df.characters.forEach(element => {
      if (element.indexOf('18') > 0) count++;
    }));
  }
  console.log(count);
});
