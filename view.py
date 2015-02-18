template_head = """
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
        .movie-row {
            margin-top: 20px;
        }
        .movie-tile {
            padding:10px;
        }
        .movie-tile:hover {
            background-color: #D8D8D8;
        }
        img.movie-cover {
            width: 203px;
            height: 300px;
        }
        img.movie-modal {
            width:100%;
        }
        div.movie-modal-info {
            padding-left:10px;
        }
    </style>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>    
        
    <script type="text/javascript" charset="utf-8">
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            if ( $(this).next(".movie-tile").length > 0 ) {
                $(this).next(".movie-tile").show("fast", showNext);
            } else {
                $(this).parent().next('.movie-row').children().first('.movie-tile').show("fast", showNext);
            }
          });
        });
    </script>
  </head>
"""
template_body = """
  <body>
    <nav class="navbar navbar-default navbar-static-top">
        <a class="navbar-brand" href="#">My Movie Website</a>
        <p class="navbar-text">Udacity project by Sam Frances</p>
    </nav>
    <div class="container">
    {content}
    </div>
"""

template_footer = """    
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
"""

movie_template = """
<div class="col-md-4 text-center movie-tile">
<img src="{poster_image_url}" class="movie-cover">
<h3>{title}</h3>
<a class="btn btn-info" href="#" role="button" data-toggle="modal" data-target="#basicModal{imdb_id}">Info</a>
<a class="btn btn-info" href="#" role="button">Trailer</a>
</div>
"""

modal_template = """
<div class="modal fade movie-modal" id="basicModal{imdb_id}" tabindex="-1" role="dialog" aria-labelledby="basicModal" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title" id="myModalLabel">{title} ({age_rating})</h4>
            </div>
            <div class="modal-body row">
                <div class="col-md-6">
                    <img src="{poster_image_url}" class="movie-modal" />
                </div>
                <div class="col-md-6 movie-modal-info">
                    <p>{storyline}</p>
                    <p><strong>IMDB Rating: </strong>{imdb_rating}</p>
                </div>
            </div>
        </div>
    </div>
  </div>
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
            html += '\n<div class="row movie-row">\n' 
        new_html = movie_template.format(poster_image_url=movie.poster_image_url,
                                         title=movie.title, 
                                         trailer_youtube_url = movie.trailer_youtube_url,
                                         imdb_id = movie.imdb_id)
        html += new_html
        if counter % 3 == 0:
            html += "\n</div>\n"
        counter += 1
    if counter % 3 != 1:
        html += "\n</div>\n"
    return html

def _modals(*movies):
    html = ''
    for movie in movies:
        new_html = modal_template.format(title= movie.title,
                                         storyline = movie.storyline,
                                         imdb_id = movie.imdb_id,
                                         age_rating = movie.age_rating,
                                         poster_image_url = movie.poster_image_url,
                                         imdb_rating = movie.imdb_rating)
        html += new_html
    return html
    
def movies_view(*movies):
    content = _content(*movies)
    modals = _modals(*movies)
    html = template_head + template_body.format(content=content) + modals + template_footer
    return html
