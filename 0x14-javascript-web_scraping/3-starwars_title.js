#!/usr/bin/node
const argument = process.argv;
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + argument[2]).then(function (response) {
  console.log(response.data.title);
});
