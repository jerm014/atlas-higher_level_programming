#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');

if (filename === undefined) process.exit(1);

fs.readFile(filename, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
