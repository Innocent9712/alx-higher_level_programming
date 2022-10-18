#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('node:fs');
const args = require('node:process').argv;

fs.readFile(args[2], 'utf-8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
