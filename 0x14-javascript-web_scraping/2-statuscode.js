#!/usr/bin/node
const argument = process.argv;
const axios = require('axios').default;

axios.get(argument[2]).then(function (response) {
  console.log('code: ' + response.status);
})
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
