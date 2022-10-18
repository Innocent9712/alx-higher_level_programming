#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const req = require('request');
const args = require('process').argv;

req.get(`https://swapi-api.hbtn.io/api/films/${args[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
