#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');

if (x === undefined)
  return false;

fs.readFile(filename, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
