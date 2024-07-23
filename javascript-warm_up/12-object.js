#!/usr/bin/node

// This one is weird. Am I missing something?
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);
myObject.value = 89;
console.log(myObject);
