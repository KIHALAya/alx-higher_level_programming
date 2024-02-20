#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

function fetchAndCountFilms (url, count = 0) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      return;
    }
    const data = JSON.parse(body);
    const films = data.results;
    count += films.reduce((acc, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        acc++;
      }
      return acc;
    }, 0);
    if (data.next) {
      fetchAndCountFilms(data.next, count);
    } else {
      console.log(count);
    }
  });
}

fetchAndCountFilms(apiUrl);
