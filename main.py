"""Script for running the movies website. This script creates the Movie 
objects, passes them to the rendering function, and starts the server to
serve the resulting html."""

from media import Movie
from view import movies_view
from server import VerySimpleServer


pans_labyrinth = Movie(imdb_id="tt0457430", 
                       trailer_youtube_id="EqYiSlkvRuw")

monty_python = Movie(imdb_id="tt0071853",
                     trailer_youtube_id="fxGqcCeV3qk")

todo_sobre_mi_madre = Movie(imdb_id="tt0185125", 
                            trailer_youtube_id="-PFVGvsTKXo")

twenty_eight = Movie(imdb_id="tt0289043",
                     trailer_youtube_id="02qibJJ0OvE")

volver = Movie(imdb_id="tt0441909",
               trailer_youtube_id="9L2AJmNoUgo")

four_lions = Movie(imdb_id="tt1341167",
                   trailer_youtube_id="Ew-SrlQ9tlI")  

goodbye_lenin = Movie(imdb_id="tt0301357",
                      trailer_youtube_id="u5hzmwGW4Ac")

two_days = Movie(imdb_id="tt2737050",
                 trailer_youtube_id="InuzW58ydyU")
                       
spirited = Movie(imdb_id="tt0245429",
                 trailer_youtube_id="ByXuk9QqQkk")

movies = [pans_labyrinth, monty_python, todo_sobre_mi_madre, volver, four_lions, twenty_eight, goodbye_lenin, two_days, spirited]

if __name__ == "__main__":
    html = movies_view(*movies)
    srv = VerySimpleServer(html)
    srv.run()
