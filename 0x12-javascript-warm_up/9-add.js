#!/usr/bin/node

function add (a, b) { console.log(a + b); }

add(+process.argv[2], +process.argv[3]);
