#!/usr/bin/node
// Write a script that writes a string to a file.
const fs = require('node:fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
