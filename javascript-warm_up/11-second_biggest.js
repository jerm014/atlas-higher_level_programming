#!/usr/bin/node

// output the second largest number from an array of numbers given.

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  // index 0 is the largest. 1 is the second largest.
  console.log(args[1]);
}
