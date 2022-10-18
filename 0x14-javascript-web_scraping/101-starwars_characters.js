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
    for (let i = 0; i < result.length; i++) {
      req.get(result[i], (err, res, body) => {
        err ? console.log(err) : console.log(JSON.parse(body).name);
      });
    }
  }
});
