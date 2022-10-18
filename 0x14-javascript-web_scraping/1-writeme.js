#!/usr/bin/node
// Write a script that writes a string to a file.
const fs = require('node:fs');
const args = require('node:process').argv;

fs.writeFile(args[2], args[3], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
