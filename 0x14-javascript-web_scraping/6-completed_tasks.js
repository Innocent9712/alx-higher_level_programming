#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const req = require('request');
const args = require('process').argv;
const list = {};

req.get(`${args[2]}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const result = JSON.parse(body);
    for (let i = 0; i < result.length; i++) {
      const completed = result[i].completed;
      const userId = result[i].userId;
      if (completed) {
        list[userId] ? (list[userId]++) : (list[userId] = 1);
      }
    }
  }
  console.log(list);
});
