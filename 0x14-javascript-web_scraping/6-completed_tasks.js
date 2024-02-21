#!/usr/bin/node

const request = require('request');

const dic = {};
request('https://jsonplaceholder.typicode.com/todos', function (error, response, body) {
  if (error) {
    console.log('error');
  }

  const bodyJson = JSON.parse(body);
  bodyJson.forEach(myFunc);

  function myFunc (item) {
    if (item.completed === true) {
      if (dic[item.userId] == null) {
        dic[item.userId] = 0;
      }
      dic[item.userId] = dic[item.userId] + 1;
    }
  }

  console.log(dic);
});
