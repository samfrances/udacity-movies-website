import urllib, json

class Movie():
    """This class represents movies and associated information."""
    
    def __init__(self, imdb_id, trailer_youtube_id, title=None, storyline=None, poster_image_url=None):
        self._omdb_data = {}
        self.trailer_youtube_id = trailer_youtube_id
        self.imdb_id = imdb_id
        if title:
            self.title = title
        if storyline:
            self.storyline = storyline
        if poster_image_url:
            self.poster_image_url = poster_image_url
        self._get_omdb_data()
    
    def _get_omdb_data(self):
        url = "http://www.omdbapi.com/?i=" + self.imdb_id + "&plot=short&r=json"
        json_data = urllib.urlopen(url).read()
        data = json.loads(json_data)
        self._omdb_data["title"] = data["Title"].encode('utf-8', 'ignore')
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
        if name in self._omdb_data:
            return self._omdb_data[name]
        else:
            raise AttributeError(name)
