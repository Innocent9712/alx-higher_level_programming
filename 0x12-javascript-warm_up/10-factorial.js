#!/usr/bin/node
const process = require('process');

function factorial (num) {
  if (num <= 1) {
    return (1);
  }
  return num * factorial(num - 1);
}

console.log((!process.argv[2] || isNaN(process.argv[2])) ? 1 : factorial(Number(process.argv[2])));
