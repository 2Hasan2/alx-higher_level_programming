#!/usr/bin/node
const request = require('request');
const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(URL, (err, res) => {
  console.log(err || JSON.parse(res.body).title);
});
