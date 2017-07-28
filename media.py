import webbrowser
class Movie():
    """ Three of my Favorite Movies to Checkout This summer """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    #def trail_youtube_id(self):
        #print(self.trailer_youtube_id = trailer_youtube_link.translate(None, "https://www.youtu.be"))

    def show_info(self):
        print("Title: "+self.title)
        print(self.poster_image_url)

    
    def show_trailer():
        webbrowser.open(self.trailer_youtube_id)

    

    
    
