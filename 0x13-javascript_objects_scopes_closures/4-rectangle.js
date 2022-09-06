#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str;
    for (let i = 0; i < this.height; i++) {
      str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
