#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, (err, res) => {
	console.log(err || `code: ${res.statusCode}`);
});
