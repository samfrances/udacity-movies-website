import media, view, server

pans_labyrinth = media.Movie(imdb_id="tt0457430", 
                             trailer_youtube_id="EqYiSlkvRuw")

monty_python = media.Movie(imdb_id="tt0071853",
                           trailer_youtube_id="fxGqcCeV3qk")

todo_sobre_mi_madre = media.Movie(imdb_id="tt0185125", 
                                  trailer_youtube_id="-PFVGvsTKXo")

twenty_eight = media.Movie(imdb_id="tt0289043",
                           trailer_youtube_id="02qibJJ0OvE")

volver = media.Movie(imdb_id="tt0441909",
                     trailer_youtube_id="9L2AJmNoUgo")

four_lions = media.Movie(imdb_id="tt1341167",
                         trailer_youtube_id="https://www.youtube.com/watch?v=nxJlqapu3zE")  

movies = [pans_labyrinth, monty_python, todo_sobre_mi_madre, volver, four_lions, twenty_eight]

if __name__ == "__main__":
    html = view.movies_view(*movies)
    srv = server.VerySimpleServer(html)
    srv.run()
