#!/usr/bin/node

const nSquare = require('./5-square');

class Square extends nSquare {
  charPrint (c) {
    for (let a = 0; a < this.height; a++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
	console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
