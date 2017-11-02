import webbrowser

class Movie():
        """This class provides a way to store movie related info."""
        VALID_RATING=['G','PG','PG-13','R']        

        def __init__(self,movie_title,movie_storyline,poster_image,trailer_website):
                """Initialize the class construction

                        Keyword arguments:
                        movie_title -- name of movie
                        movie_storyline -- storyline of movie
                        poster_image -- url of movie's poster image
                        trailer_website -- url of movie trailer                       
                """
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_website

        def show_trailer(self):
                """Open Trailer url in website

                        Keyword arguments:
                        self -- calss self
                """                               
                webbrowser.open(self.trailer_website_url)
