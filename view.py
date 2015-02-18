main_template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Movie Website</title>

    <!-- Bootstrap -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet">

    <!-- My extra styles -->
    <style>
        .top20 {{
            margin-top:20px;
        }}
    </style>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
  
    <div class="container">
    {content}
    </div>
    
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
"""

movie_template = """
<div class="col-md-4">
<img src="{poster_image_url}" style="height:300px;">
</div>
"""

movie_template_old = """
<div style="overflow:auto;background-color:lightgrey;padding:10px;margin-bottom:10px;">
<img src="{poster_image_url}" style="float:left;padding-right:20px;">
<h1>{title}</h1>
<p>{storyline}</p>
<p><strong>Age rating:</strong> {age_rating}</p>
<p><strong>IMDB rating:</strong> {imdb_rating}</p>
<p><a href="{trailer_youtube_url}" target="_blank">View trailer on Youtube</a></p>
</div>
"""

def _content(*movies):
    html = ''
    counter = 1
    for movie in movies:
        if (counter % 3) == 1:
            html += '\n<div class="row top20">\n' 
        new_html = movie_template.format(poster_image_url=movie.poster_image_url,
                                         title=movie.title,
                                         storyline=movie.storyline,
                                         age_rating=movie.age_rating,
                                         imdb_rating=movie.imdb_rating,
                                         trailer_youtube_url = movie.trailer_youtube_url)
        html += new_html
        if counter % 3 == 0:
            html += "\n</div>\n"
        counter += 1
    if counter % 3 != 1:
        html += "\n</div>\n"
    return html

def movies_view(*movies):
    content = _content(*movies)
    html = main_template.format(content=content)
    return html
