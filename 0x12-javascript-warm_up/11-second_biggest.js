#!/usr/bin/node
const process = require('process');
const newArr = process.argv.slice(2);

if (newArr.length < 2) {
  console.log(0);
} else {
  console.log(newArr.sort()[newArr.length - 2]);
}
