#!/usr/bin/node
const process = require('process');
let count;

if (Number(process.argv[2])) {
  count = Number(process.argv[2]);

  for (let index = 0; index < count; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
