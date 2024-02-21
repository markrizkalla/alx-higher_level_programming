#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasks = tasks.reduce((completed, task) => {
    if (task.completed) {
      completed[task.userId] = (completed[task.userId] || 0) + 1;
    }
    return completed;
  }, {});

  console.log(completedTasks);
});
