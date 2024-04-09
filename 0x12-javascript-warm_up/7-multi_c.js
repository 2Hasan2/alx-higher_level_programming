#!/usr/bin/node

const x = +process.argv[2];

if (isNaN(x)) console.log('Missing number of occurrences');
else Array(x).fill('C is fun').forEach(ele => console.log(ele));
