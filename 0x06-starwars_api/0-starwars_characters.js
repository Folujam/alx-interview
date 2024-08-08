#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, body) {
  if (err) throw err;
  const charactars = JSON.parse(body).characters;
  exactOrder(charactars, 0);
});
// define exactOrder fxn that gets xters,print 1 on 1line
const exactOrder = (characters, x) => {
  if (x === characters.length) return;
  request(characters[x], function (err, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(characters, x + 1);
  });
};
