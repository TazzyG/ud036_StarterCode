import fresh_tomatoes
import media

# seperate file to call the methods

you_been_trumped = media.Movie("You've Been Trumped", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIzMjE3MDcwM15BMl5BanBnXkFtZTcwMjk0Mjg4Ng@@._V1_UY268_CR4,0,182,268_AL_.jpg", "https://www.youtu.be/hjAIKgOOc8A")
war_of_the_planet_of_the_apes = media.Movie("War of the Planet of the Apes", "https://resizing.flixster.com/2UmR2Oly25tyYghNuAHD1tl7XBA=/206x305/v1.bTsxMjQxNTA3MztqOzE3NDIzOzEyMDA7Mjk2NDs0Mzkx", "https://www.youtu.be/qxjPjPzQ1iU")
detroit = media.Movie("Detroit", "https://resizing.flixster.com/kgXSy4E7N2K4Da2EGzHuZ4EzJXw=/206x305/v1.bTsxMjQ1NDA0NjtqOzE3NDI0OzEyMDA7NTQwOzgwMA", "https://www.youtu.be/d5h7Kgo-zeI")

movies = [you_been_trumped, war_of_the_planet_of_the_apes, detroit]

#print(media.Movie.__doc__)
#print(media.Movie.__dict__)
#print(media.Movie.__name__)

fresh_tomatoes.open_movies_page(movies)



