#!/usr/bin/node
let num = +process.argv[2]
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
