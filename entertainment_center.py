import media
import fresh_tomatoes

the_dark_knight = media.Movie("The Dark Knight", "Out of the darkness...comes the Knight.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                              "https://youtu.be/5y2szViJlaY")

finding_nemo = media.Movie("Finding Nemo", "There are 3.7 trillion fish in the ocean,"
                           "they're looking for one.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg",
                           "https://youtu.be/wZdpNglLbt8")

rudy = media.Movie("Rudy", "Sometimes a winner is a dreamer who just won't quit",
                   "https://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",
                   "https://youtu.be/eDKOlH0I0nQ")

remember_the_titans = media.Movie("Remember the Titans", "Before they could win, they had to become one.",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Remember_the_titansposter.jpg/220px-Remember_the_titansposter.jpg",
                                  "https://youtu.be/nPhu9XsRl4M")

the_peanuts_movie = media.Movie("The Peanuts Movie", "Dream big",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/Peanuts_2015.jpg/220px-Peanuts_2015.jpg",
                                "https://youtu.be/fVR4E6Q6u5g")

the_two_towers = media.Movie("Lord of the Rings: The Two Towers", "The Battle for Middle-earth Begins!",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg/220px-Lord_of_the_Rings_-_The_Two_Towers.jpg",
                             "https://youtu.be/cvCktPUwkW0")

movies = [the_peanuts_movie, the_dark_knight, rudy,
          remember_the_titans, finding_nemo, the_two_towers]
fresh_tomatoes.open_movies_page(movies)
