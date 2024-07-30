#!/usr/bin/node
const filename = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

if ((filename === undefined) || (data === undefined)) process.exit(1);

fs.writeFile(filename, data, (err) => {if (err) console.log(err)});
