#!/usr/bin/node

const fs = require('node:fs');
const args = require('node:process').argv;

fs.readFile(args[2], 'utf-8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
