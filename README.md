# Udacity Movie Trailer Website Project

## About

This is my submission for **Project P1: Movie Trailer Website**, part of Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004).

The project brief is as follows:

> You will write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. You will then serve this data as a web page allowing visitors to review their movies and watch the trailers.

My movie trailer website automatically downloads movie information from the [Open Movie Database](http://www.omdbapi.com/), so Movie objects need only be initialised with an Internet Movie Database ID and a Youtube video ID for the trailer.

## How to run

1. Run `python main.py` in the terminal.
2. Open [http://localhost:8080/](http://localhost:8080/) in your preferred browser.

## Third-party code
* Libraries and frameworks
  - Bootstrap v3.3.2
  - jQuery v1.11.2
* view.py uses:
  - a modified version of the Bootstrap Basic Template from http://getbootstrap.com/getting-started/
  - a modified version of the $(document).ready function from https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py
  - a modified version of the modal dialogue template from http://www.sitepoint.com/understanding-bootstrap-modals/
  - this layout solution in information modals: http://stackoverflow.com/a/19615212
  - code for embedded youtube player: https://developers.google.com/youtube/player_parameters#Embedding_a_Player
