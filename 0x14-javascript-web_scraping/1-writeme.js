#!/usr/bin/node
const argument = process.argv;
const fs = require('fs');

fs.writeFile(argument[2], argument[3], 'utf8', (error, response) => {
  if (error) {
    console.error(error);
  }
});

