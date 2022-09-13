#!/usr/bin/node
const argument = process.argv;
const axios = require('axios').default;
const fs = require('fs');

axios.get(argument[2]).then(function (response) {
  fs.writeFile(argument[3], response.data, error => {
    if (error) {
      console.error(error);
    }
  });
})
