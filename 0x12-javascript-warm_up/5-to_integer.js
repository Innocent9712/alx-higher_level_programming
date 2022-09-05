#!/usr/bin/node
const process = require('process');
console.log(`${Number(process.argv[2]) ? `My number: ${Math.floor(Number(process.argv[2]))}` : 'Not a number'}`);
