#!/usr/bin/node
const process = require('process');
let count, cross;

if (Number(process.argv[2])) {
  count = Number(process.argv[2]);

  for (let index = 0; index < count; index++) {
    cross = '';
    for (let index = 0; index < count; index++) {
      cross += 'X';
    }
    console.log(cross);
  }
} else {
  console.log('Missing size');
}
