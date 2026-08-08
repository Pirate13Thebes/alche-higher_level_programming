#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.filter((film) => film.characters.some((character) => character.endsWith(`/${characterId}/`))).length;
  console.log(count);
});
