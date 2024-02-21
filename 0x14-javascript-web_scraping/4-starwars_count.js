#!/usr/bin/node

const request = require('request');
request(`${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  let appreance = 0;
  body = JSON.parse(body).results;
  body.forEach(myFunction);
  function myFunction (item) {
    item.characters.forEach(mySecFun);
  }

  function mySecFun (charac) {
    if (charac === 'https://swapi-api.alx-tools.com/api/people/18/') {
      appreance++;
    }
  }
  console.log(appreance);
});
