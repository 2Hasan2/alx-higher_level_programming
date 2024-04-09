const { argv } = require('node:process');

console.log(argv.length == 2 ? 'No argument' : 'Argument found');
