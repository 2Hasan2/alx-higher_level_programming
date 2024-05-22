#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter(task => task.completed === true);
    const completedTasksByUser = completedTasks.reduce((acc, task) => {
      if (acc[task.userId]) {
        acc[task.userId]++;
      } else {
        acc[task.userId] = 1;
      }
      return acc;
    }, {});

    console.log(completedTasksByUser);
  }
});
