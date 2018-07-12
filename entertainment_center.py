import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A stry of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")
#print(toy_story.storyline)
#toy_story.show_trailer()
frozen = media.Movie("Frozen",
                     "A story about a girl who finds out she has magics while still young",
                     "https://upload.wikimedia.org/wikipedia/commons/e/e4/Kristen_Bell_at_Frozen_premiere%2C_El_Capitan_Theatre.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

spiderman = media.Movie("SpiderMan",
                     "Spider-Man is a fictional superhero appearing in American comic books published by Marvel Comics. The character was created by writer-editor Stan Lee and writer-artist Steve Ditko, and first appeared",
                     "https://upload.wikimedia.org/wikipedia/commons/9/95/Spider-Man2.jpg",
                     "https://www.youtube.com/watch?v=U0D3AOldjMU")
Moana = media.Movie("Moana",
                    "An adventurous teenager sails out on a daring mission to save her people. During her journey, Moana meets the once-mighty demigod Maui, who guides her in her quest to become a master way-finder. Together they sail across the open ocean on an action-packed voyage, encountering enormous monsters",
                    "https://upload.wikimedia.org/wikipedia/commons/1/16/Moana.svg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")
movies = [toy_story, frozen, spiderman, Moana]
fresh_tomatoes.open_movies_page(movies)
