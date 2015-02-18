"""A module which provides a class for retrieving, storing and representing 
information about movies"""

import urllib, json

class Movie():
    """This class represents movies and associated information."""
    
    def __init__(self, imdb_id, trailer_youtube_id,
                 title=None,
                 storyline=None,
                 poster_image_url=None,
                 age_rating=None,
                 imdb_rating=None,
                 genre=None,
                 directors=None,
                 actors=None,
                 awards=None,
                 release_date=None):
        # Mandatory attributes
        self.trailer_youtube_id = trailer_youtube_id
        self.imdb_id = imdb_id
        # Optional attributes
        if title:
            self.title = title
        if storyline:
            self.storyline = storyline
        if poster_image_url:
            self.poster_image_url = poster_image_url
        if age_rating:
            self.age_rating = age_rating
        if imdb_rating:
            self.imdb_rating = imdb_rating
        if genre:
            self.genre = genre
        if directors:
            self.directors = directors
        if actors:
            self.actors = actors
        if awards:
            self.awards = awards
        if release_date:
            self.release_date = release_date
        # Initialise dict for Open Movie Database data and fetch data
        self._omdb_data = {}
        self._get_omdb_data()
    
    def _get_omdb_data(self):
        """Fetch data from the Open Movie Database and cache that data"""
        url = "http://www.omdbapi.com/?i=" + self.imdb_id + "&plot=short&r=json"
        json_data = urllib.urlopen(url).read()
        data = json.loads(json_data)
        self._omdb_data["title"] = data["Title"].encode('utf-8', 'ignore') # encode to prevent encoding errors
        self._omdb_data["storyline"] = data["Plot"].encode('utf-8', 'ignore')
        self._omdb_data["poster_image_url"] = data["Poster"].encode('utf-8', 'ignore')
        self._omdb_data["age_rating"] = data["Rated"].encode('utf-8', 'ignore')
        self._omdb_data["imdb_rating"] = float(data["imdbRating"])
        self._omdb_data["genre"] = data["Genre"].encode('utf-8', 'ignore')
        self._omdb_data["directors"] = data["Director"].encode('utf-8', 'ignore').split(", ")
        self._omdb_data["actors"] = data["Actors"].encode('utf-8', 'ignore').split(", ")
        self._omdb_data["awards"] = data["Awards"].encode('utf-8', 'ignore')
        self._omdb_data["release_date"] = data["Released"].encode('utf-8', 'ignore')
        
    def __getattr__(self, name):
        """Allows data to be retrieved from omdb cache via instance attributes,
        unless those attributes have been overriden"""
        if name in self._omdb_data:
            return self._omdb_data[name]
        else:
            raise AttributeError(name)
