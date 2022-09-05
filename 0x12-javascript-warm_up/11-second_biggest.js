#!/usr/bin/node
const process = require('process');
const newArr = process.argv.slice(2);
let nextMax = 0
if (newArr.length > 1) {
  newArr.sort();
  nextMax = newArr[newArr.length - 2];
}
console.log(nextMax);