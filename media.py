import urllib, json

class Movie():
    """This class represents movies and associated information."""
    
    def __init__(self, imdb_id=None, trailer_youtube=None, title=None, storyline=None, poster_image=None):
        self._omdb_data = {}
        if title:
            self.title = title
        if storyline:
            self.storyline = storyline
        if poster_image:
            self.poster_image = poster_image
        if trailer_youtube:
            self.trailer_youtube = trailer_youtube
        if imdb_id:
            self.imdb_id = imdb_id
        self._get_omdb_data()
    
    def _get_omdb_data(self):
        url = "http://www.omdbapi.com/?i=" + self.imdb_id + "&plot=short&r=json"
        json_data = urllib.urlopen(url).read()
        data = json.loads(json_data)
        self._omdb_data["title"] = data["Title"]
        self._omdb_data["storyline"] = data["Plot"]
        self._omdb_data["poster_image"] = data["Poster"]
        self._omdb_data["age_rating"] = data["Rated"]
        self._omdb_data["imdb_rating"] = float(data["imdbRating"])
    
    def __getattr__(self, name):
        if name in self._omdb_data:
            return self._omdb_data[name]
        else:
            raise AttributeError(name)