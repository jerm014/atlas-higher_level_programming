#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let rows = 0; i < this.height; rows++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
