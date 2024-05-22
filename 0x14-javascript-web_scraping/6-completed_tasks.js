#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, _, body) => {
  if (err) return console.error(err);

  const tasks = JSON.parse(body);
  const completed = tasks.filter(task => task.completed)
                         .reduce((acc, task) => {
                           acc[task.userId] = (acc[task.userId] || 0) + 1;
                           return acc;
                         }, {});
  
  console.log(completed);
});
