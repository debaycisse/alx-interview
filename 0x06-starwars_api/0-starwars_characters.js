#!/usr/bin/node
/* This script fetches a list of characters' names for a given movie ID */
const request = require('request');

const movieID = parseInt(process.argv[2]);

if (isNaN(movieID)) {
  console.log(`Usage: ${process.argv[1]} <movie's id>`);
  process.exit(1);
}

async function fetchCharacterObject (characterUrl) {
  /* Fetches a character's object whose url is given */
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const data = JSON.parse(body);
        resolve(data);
      } else {
        reject(new Error('Could not fetch - ', characterUrl));
      }
    });
  });
}

async function fetchCharacterNames (characterUrls) {
  /* Fetches and prints out all names of characters whose urls are given */
  for (const url of characterUrls) {
    try {
      const characterObject = await fetchCharacterObject(url);
      const characterName = characterObject.name;
      console.log(characterName);
    } catch (error) {
      console.error('Error occured while fetching user data.', error.message);
    }
  }
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request(url,
  (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characterUrls = JSON.parse(body).characters;
      fetchCharacterNames(characterUrls);
    } else {
      console.error(`Movie ID ${movieID} not found`);
    }
  }
);
