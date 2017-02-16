import media
import fresh_tomatoes

# Create movie objects
the_dark_knight = media.Movie("The Dark Knight",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",  # NOQA
                              "https://youtu.be/5y2szViJlaY")

finding_nemo = media.Movie("Finding Nemo",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg",  # NOQA
                           "https://youtu.be/wZdpNglLbt8")

rudy = media.Movie("Rudy",
                   "https://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",
                   "https://youtu.be/eDKOlH0I0nQ")

remember_the_titans = media.Movie("Remember the Titans",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Remember_the_titansposter.jpg/220px-Remember_the_titansposter.jpg",  # NOQA
                                  "https://youtu.be/nPhu9XsRl4M")

the_peanuts_movie = media.Movie("The Peanuts Movie",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/Peanuts_2015.jpg/220px-Peanuts_2015.jpg",  # NOQA
                                "https://youtu.be/fVR4E6Q6u5g")

the_two_towers = media.Movie("Lord of the Rings: The Two Towers",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg/220px-Lord_of_the_Rings_-_The_Two_Towers.jpg",  # NOQA
                             "https://youtu.be/cvCktPUwkW0")

# Add movies to the movies array
movies = [the_peanuts_movie, the_dark_knight, rudy,
          the_two_towers, remember_the_titans, finding_nemo]
# Pass the movies array to the open_movies_page method of fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
