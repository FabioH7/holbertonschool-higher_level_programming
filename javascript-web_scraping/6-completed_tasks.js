#!/usr/bin/node
const request = require('request');
const apiCall = process.argv[2];
request.get(apiCall, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const obj = {};
  let isComplete = 0;
  const data = JSON.parse(body);
  for (const elem of data) {
    isComplete = data.filter(
      (todo) => todo.userId === elem.userId && todo.completed
    ).length;
    if (isComplete === 0) {
      console.log(obj);
      return;
    } else {
      obj[elem.userId] = isComplete;
    }
  }
  console.log(obj);
});
