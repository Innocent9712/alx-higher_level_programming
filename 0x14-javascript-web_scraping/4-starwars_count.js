#!/usr/bin/node
// Write a script that prints the number of movies where the character
// “Wedge Antilles” is present.
const req = require('request');
const args = require('process').argv;
let count = 0;

req.get(`${args[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const result = JSON.parse(body).results;
    for (let index = 0; index < result.length; index++) {
      const item = result[index].characters;
      for (let j = 0; j < item.length; j++) {
        const val = item[j].split('/');
        if (val[val.length - 2] === '18') {
          count++;
          break;
        }
      }
    }
  }
  console.log(count);
});
