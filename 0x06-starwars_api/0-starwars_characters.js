#!/usr/bin/node
/* This script fetches a list of characters' names for a given movie ID */
const request = require('request');

try {
  const movieID = parseInt(process.argv[2]);
} catch (error) {
  console.error(error);
  return;
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request(url, 
  (error, response, body) => {
    if (!error && response.statusCode === 200) {
       const characterUrls = JSON.parse(body).characters;
       for (const characterUrl of characterUrls) {
         const characterData = new Promise((resolve, reject) => {
           
	 });
         const characterName = await characterData.name
       }
    }
  }
);












































async function fetchData(data, fromUrl){
  /*Fetches a given data frm a given url*/
  
}


async function fetchCharacters(movieID) {
  /**
   * Fetches a list of names of the characters for the given movie's id
   */
  try {
    request(`https://swapi-api.alx-tools.com/api/films/${movieID}`, async (error, res, body) => {
      if (!error && res.statusCode === 200) {
        const characterUrls = JSON.parse(body).characters;
        for (const characterUrl of characterUrls) {
          try {
            await request(characterUrl, (err, resp, resBody) => {
              if (!error && resp.statusCode === 200) {
                const characterName = JSON.parse(resBody).name;
                console.log(characterName)
	      }
	    });
          } catch (error) {
            console.error(error.message);
          }
        }
      }
    });
  } catch (error) {
    console.error(error.message)
  }
}

fetchCharacters(process.argv[2]);
