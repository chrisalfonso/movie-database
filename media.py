import webbrowser

class Movie():
    """Creates movie tiles with descriptions.

    Attributes:
        movie_title (str): Full movie title
        movie_storyline (str): Brief caption of movie's storyline
        poster_image (str): URL to movie poster image
        trailer_youtube (str): URL to movie trailer
        actors (str): starring cast
        release_date (str): North American launch date
        run_time (str): movie length
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                 actors, release_date, run_time):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = actors
        self.release_date = release_date
        self.run_time = run_time
