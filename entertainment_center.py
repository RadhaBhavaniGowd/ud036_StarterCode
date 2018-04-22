import media
import fresh_tomatoes

# creating Toy Story movie instance
toy_story = media.Movie(
 "Toy Story",
 "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# creating Avtar movie instance
avtar = media.Movie(
 "avatar",
 "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# creating School of rock movie instance
school_of_rock = media.Movie(
 "School of Rock",
 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
 "https://www.youtube.com/watch?v=3PsUJFEBC74")

# creating Ratatouille movie instance
ratatouille = media.Movie(
 "Ratatouille",
 "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
 "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# creating Midnight in Paris movie instance
midnight_in_paris = media.Movie(
 "Midnight in Paris",
 "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
 "https://www.youtube.com/watch?v=BYRWfS2s2v4")

# creating Hunger Games movie instance
hunger_games = media.Movie(
 "The Hunger Games",
 "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
 "https://www.youtube.com/watch?v=3PkkHsuMrho")

# creating Bharat Ane Nenu movie instance
bharat = media.Movie(
 "Bharat Ane Nenu",
 "https://upload.wikimedia.org/wikipedia/en/6/68/Bharat_Ane_Nenu_poster.jpg",
 "https://www.youtube.com/watch?v=eFciUnNvdOo")

# creating Bahubali movie instance
bahubali = media.Movie(
 "Bahubali",
 "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
 "https://www.youtube.com/watch?v=sOEg_YZQsTI")

# Adding all movie instances to list to access easily
movies = [bharat, bahubali, avtar, ratatouille,
          midnight_in_paris, hunger_games, toy_story,
          school_of_rock]

# Passing movie list to display as part of html page
fresh_tomatoes.open_movies_page(movies)
