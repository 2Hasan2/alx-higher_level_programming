#!/usr/bin/node
const request = require('request');
const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(URL, function (err, res) {
  if (err) {
    console.log(err);
    return;
  }
  const filmResult = JSON.parse(res.body);
  filmResult.characters.forEach(item => {
    request(item, function (err, res) {
      console.log(JSON.parse(err || res.body).name);
    });
  });
});
