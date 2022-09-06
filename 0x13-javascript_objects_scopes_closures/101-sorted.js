#!/usr/bin/node
const dict = require('./101-data').dict;

function sorted (dictionary) {
  const sortedDict = {};
  for (const key in dictionary) {
    if (!sortedDict[dictionary[key]]) {
      sortedDict[dictionary[key]] = [];
    }
    sortedDict[dictionary[key]].push(key);
  }
  return (sortedDict);
}

console.log(sorted(dict));
