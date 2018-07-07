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
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

avatar = media.Movie("Avatar",
                     "its an avatar movie. big story big movie",
                     "https://commons.wikimedia.org/wiki/Category:Avatar_(2009_film)#/media/File:82nd_Academy_Awards,_Stephen_Lang_-_army_mil-66457-2010-03-09-180303.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM&t=1s")
movies = [toy_story, frozen, avatar]
fresh_tomatoes.open_movies_page(movies)
