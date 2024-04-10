#!/usr/bin/node
const fs = require('fs');

const [fArg, sArg, output] = process.argv.slice(2);
fs.writeFileSync(output, fs.readFileSync(fArg) + fs.readFileSync(sArg));
