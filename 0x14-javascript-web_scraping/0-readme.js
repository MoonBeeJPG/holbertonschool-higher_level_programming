#!/usr/bin/node
const argument = process.argv;
const fs = require('fs');

fs.readFile(argument[2], 'utf8', (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response);
  }
});
