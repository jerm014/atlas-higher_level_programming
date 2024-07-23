#!/usr/bin/node
const addendOne = parseInt(process.argv[2]);
const addendTwo = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(addendOne, addendTwo));
