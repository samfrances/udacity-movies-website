main_template = """
<!doctype html>

<html>

    <head>
        <title>My Movie Website</title>
        <meta charset="utf-8" />
    </head>

    <body>
        {content}    
    </body>

</html>
"""

movie_template = """
<img src="{poster_image_url}" style="float:left">
<h1>{title}</h1>
<p>{storyline}</p>
<p><strong>Age rating:</strong>{age_rating}</p>
<p><strong>IMDB rating:</strong>{imdb_rating}</p>
<hr />
"""

def _content(*movies):
    html = ''
    for movie in movies:
        new_html = movie_template.format(poster_image_url=movie.poster_image_url,
                                         title=movie.title,
                                         storyline=movie.storyline,
                                         age_rating=movie.age_rating,
                                         imdb_rating=movie.imdb_rating)
        html += new_html
    return html

def movies_view(*movies):
    content = _content(*movies)
    html = main_template.format(content=content)
    return html
