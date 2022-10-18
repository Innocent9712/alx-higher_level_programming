#!/usr/bin/node
// Write a script that display the status code of a GET request.
const req = require('request');
const args = require('process').argv;

req.get(args[2]).on('response', (res) => console.log('code:', res.statusCode));
