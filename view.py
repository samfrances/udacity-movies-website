"""Module provides the movies_view function, which takes any number of
Movie objects, and returns html for a webpage to display the information
contained by those Movie objects."""

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
            padding-left: 10px;
        }
        .bot20 {
            margin-bottom: 20px;
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
        // Makes movie tiles appear one by one when the page loads.
        // Adapted from version in https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py 
        $(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            if ( $(this).next(".movie-tile").length > 0 ) {
                $(this).next(".movie-tile").show("fast", showNext);
            } else {
                $(this).parent().next('.movie-row').children().first('.movie-tile').show("fast", showNext);
            }
          });
        });
        
        // Adds functionality to 'Trailer' buttons, so that when clicked
        // they open a modal embedding a Youtube video of the trailer.
        // Uses information stored in data attributes of the buttons.
        $(function() {
            $('.trailer-button').each(function() {
                // Get info from button's data attributes
                var youtube_id = $(this).data("youtube_id");
                var modal_id = $(this).data("target");
                var title = $(this).data("title");
                var age_rating = $(this).data("age_rating");
                
                // Form html for embedded youtube player
                var html = '<iframe id="ytplayer" type="text/html" width="550" height="390" src="http://www.youtube.com/embed/'
                html += youtube_id
                html += '?autoplay=1" frameborder="0"/>'
                
                // Set click event handler for button, so that is opens the
                // trailer modal, and changes the modal heading and content so as to
                // play the right trailer.
                $(this).click(function() {
                    var modal = $(modal_id);
                    modal.find('.modal-body').html(html);
                    modal.find('.modal-title').text(title + " (" + age_rating +")");
                })
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
    <div class="container bot20">
    {content}
    </div>
    
    <!-- Trailer modal -->
    <div class="modal fade" id="trailerModal" tabindex="-1" role="dialog" aria-labelledby="basicModal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title" id="myModalLabel"></h4>
                </div>
                <div class="modal-body text-center"></div>
            </div>
        </div>
      </div>
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

<!-- Info modal IDs contain the imdb_id, so this can be used to target the correct modal -->
<a class="btn btn-info" href="#" role="button" data-toggle="modal" data-target="#basicModal{imdb_id}">Info</a>

<!-- Button contains data passed to trailer modal -->
<a class="btn btn-info trailer-button" 
   href="#"
   role="button" 
   data-toggle="modal" 
   data-target="#trailerModal" 
   data-youtube_id="{trailer_youtube_id}"
   data-title="{title}"
   data-age_rating="{age_rating}">Trailer</a>
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
                    <p><strong>Released: </strong>{release_date}</p>
                    <p><strong>Genre: </strong>{genre}</p>
                    <p><strong>Directors: </strong>{directors}</p>
                    <p><strong>Actors: </strong>{actors}</p>
                    <p><strong>Awards: </strong>{awards}</p>
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
    """Renders Movie objcets into html for bootstrap rows and tiles"""
    html = ''
    counter = 1
    for movie in movies:
        if (counter % 3) == 1:
            html += '\n<div class="row movie-row">\n' 
        new_html = movie_template.format(poster_image_url=movie.poster_image_url,
                                         title=movie.title, 
                                         trailer_youtube_id = movie.trailer_youtube_id,
                                         imdb_id = movie.imdb_id,
                                         age_rating = movie.age_rating)
        html += new_html
        if counter % 3 == 0:
            html += "\n</div>\n"
        counter += 1
    if counter % 3 != 1:
        html += "\n</div>\n"
    return html

def _modals(*movies):
    """Renders Movie objects into bootstrap modals for displaying movie info"""
    html = ''
    for movie in movies:
        new_html = modal_template.format(title = movie.title,
                                         storyline = movie.storyline,
                                         imdb_id = movie.imdb_id,
                                         age_rating = movie.age_rating,
                                         poster_image_url = movie.poster_image_url,
                                         imdb_rating = movie.imdb_rating,
                                         genre = movie.genre,
                                         directors = ', '.join(movie.directors),
                                         actors = ', '.join(movie.actors),
                                         awards = movie.awards,
                                         release_date = movie.release_date)
        html += new_html
    return html
    
def movies_view(*movies):
    """Renders html webpage displaying information stored in Movie objects."""
    content = _content(*movies)
    modals = _modals(*movies)
    html = template_head + template_body.format(content=content) + modals + template_footer
    return html
