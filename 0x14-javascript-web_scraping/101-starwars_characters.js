#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${ process.argv[2]}`;
request(url, function (err, _, body) {
  if (!err) {
    printCharacters(JSON.parse(body).characters, 0);
  }
});

function printCharacters (char, index) {
  request(char[index], function (error, _, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < char.length) {
        printCharacters(char, index + 1);
      }
    }
  });
}