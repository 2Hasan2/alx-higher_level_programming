#!/usr/bin/node

const x = +process.argv[2]

console.log(isNaN(x) ? "Missing number of occurrences" : "C is fun\n".repeat(x).trim());
