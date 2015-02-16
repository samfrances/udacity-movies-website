import urllib, json

class Movie():
    """This class represents movies and associated information."""
    
    def __init__(self, imdb_id=None, trailer_youtube=None, title=None, storyline=None, poster_image=None):
        self._omdb_data = {}
        if title:
            self._title = title
        if storyline:
            self._storyline = storyline
        if poster_image:
            self._poster_image = poster_image
        if trailer_youtube:
            self._trailer_youtube = trailer_youtube
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
    
    @property
    def title(self):
        if hasattr(self, '_title'):
            return self._title
        return self._omdb_data["title"]
    
    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def storyline(self):
        if hasattr(self, '_storyline'):
            return self._storyline
        return self._omdb_data["storyline"]
    
    @storyline.setter
    def storyline(self, value):
        self._storyline = value
    
    @property
    def poster_image(self):
        if hasattr(self, '_poster_image'):
            return self._poster_image
        return self._omdb_data["poster_image"]
    
    @poster_image.setter
    def poster_image(self, value):
        self._poster_image = value
