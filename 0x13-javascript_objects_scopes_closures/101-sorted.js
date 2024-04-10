#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = Object.entries(dict).reduce((acc, [userId, occurrences]) => {
  acc[occurrences] = acc[occurrences] ? [...acc[occurrences], userId] : [userId];
  return acc;
}, {});

console.log(sortedDict);
