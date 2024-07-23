#!/usr/bin/node
let i = process.argv[2];

if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (; i > 0; i--) {
    console.log('C is fun');
  }
}
