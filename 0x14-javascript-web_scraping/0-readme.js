#!/usr/bin/node
const argument = process.argv;
const request = require('request');

request.readFile(argument[2], 'utf8', (error, response) => {
 if (error) {
  console.error(error);
  return
 } else {
  console.log(response);
 }
});
