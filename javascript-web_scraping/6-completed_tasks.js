#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let results;
const output = {};

if (url === undefined) process.exit(1);
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    results = JSON.parse(body).filter((resfil) => resfil.completed);
    results.forEach(node => {
      if (output[node.userId]) {
        output[node.userId] += 1;
      } else { 
        output[node.userId] = 1;
      }
    });
    console.log(output);
  }
});
