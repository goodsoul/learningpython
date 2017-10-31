import webbrowser

class Movie():
        """This class provides a way to store movie related info."""
        VALID_RATING=['G','PG','PG-13','R']        
        
        def __init__(self,movie_title,movie_storyline,poster_image,trailer_website):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_website

        def show_trailer(self):
            webbrowser.open(self.trailer_website_url)
