#!/usr/bin/node
const addend_1 = parseInt(process.argv[2]);
const addend_2 = parseInt(process.argv[3]);

function add (a, b) {
  const total = a + b;
  return (total);
}

console.log(add(addend_1, addend_2));
