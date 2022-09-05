#!/usr/bin/node
const process = require('process');
const args = process.argv.length;
if (args === 2) {
  console.log('No argument');
} else {
  console.log(`Argument${args > 3 ? 's' : ''} found`);
}
