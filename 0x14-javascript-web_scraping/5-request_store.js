#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.
const fs = require('node:fs');
const args = require('process').argv;
const req = require('request');

req.get(`${args[2]}`).pipe(fs.createWriteStream(args[3], 'utf-8'));
