#Movie Class which stores Title, Image Url and Youtube Trailer Url
class Movie():

    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, image_url, trailer_url):
		self.title = movie_title
		self.poster_image_url = image_url
		self.trailer_youtube_url = trailer_url