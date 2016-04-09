import render_movies
import media

star_wars = media.Movie("Star Wars Episode IV",
                        "In a galaxy far, far away...",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                        "Mark Hamill, Harrison Ford, Carrie Fisher",
                        "1977",
                        "2h 1min")

star_trek = media.Movie("Star Trek",
                        "Boldly going where no one has gone before",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                        "https://www.youtube.com/watch?v=pKFUZ10Wmbw",
                        "Chris Pine, Zachary Quinto, Simon Pegg",
                        "2009",
                        "2h 7min")

gravity = media.Movie("Gravity",
                      "Space panic",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=ufsrgE0BYf0",
                      "Sandra Bullock, George Clooney",
                      "2013",
                      "1h 31min")

avengers = media.Movie("Avengers",
                       "Superheroes unite",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                       "Robert Downey Jr., Chris Evans, Scarlett Johansson",
                       "2012",
                       "2h 23min")

casino_royale = media.Movie("Casino Royale",
                            "Down with Le Chiffre",
                            "http://www.gstatic.com/tv/thumb/movieposters/159167/p159167_p_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=xK7PbujRUOk",
                            "Daniel Craig, Eva Green, Judi Dench",
                            "2006",
                            "2h 24min")

bourne_identity = media.Movie("The Bourne Identity",
                              "Jason Bourne has amnesia, but kicks ass",
                              "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                              "https://www.youtube.com/watch?v=cD-uQreIwEk",
                              "Franka Potente, Matt Damon, Chris Cooper",
                              "2002",
                              "1h 59min")

# Collect all movies to create tiles for on webpage
my_movies = [star_wars, star_trek, gravity, avengers, casino_royale, bourne_identity]

# Create a tile for each movie and generate a webpage
render_movies.open_movies_page(my_movies)
