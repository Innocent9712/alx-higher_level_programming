#!/usr/bin/node
const process = require('process');
const fs = require('fs');

if (process.argv.length === 5) {
  const args = process.argv;

  function readFile (path) {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        console.error(err);
        return;
      }
      writeFile(args[4], data);
    });
  }

  function writeFile (path, content) {
    fs.writeFile(path, content, { flag: 'a' }, err => {
      if (err) {
        console.log(err);
      }
    });
  }

  readFile(args[2]);
  readFile(args[3]);
}
