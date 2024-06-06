#!/usr/bin/node

const request = require('request');

// Check if a movie ID was provided
if (process.argv.length !== 3) {
  console.log('Usage: ./3-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the API endpoint for the specified movie
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the API to get the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const movie = JSON.parse(body);

  // Check if the movie was found
  if (response.statusCode === 404) {
    console.log('Movie not found');
    process.exit(1);
  }

  // Get the list of characters
  const characters = movie.characters;

  // Fetch and print the names of the characters
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the JSON response
      const character = JSON.parse(body);

      // Print the name of the character
      console.log(character.name);
    });
  });
});
