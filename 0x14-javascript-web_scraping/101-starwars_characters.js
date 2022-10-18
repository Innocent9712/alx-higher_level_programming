#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const req = require('request');
const args = require('process').argv;
const api = 'https://swapi-api.hbtn.io/api';

req.get(`${api}/films/${args[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const result = JSON.parse(body).characters;
    printCharacters(result, 0);
  }
});

function printCharacters (characters, index) {
  req(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
