favorite_movies = ("Inception", "Interstellar", "The Dark Knight", "Memento", "Tenet", "Dunkirk")

first_movie, *remaining_movies = favorite_movies

print("-------------------Unpack Tuples-------------------")
print("პირველი ფილმი: ", first_movie)
print("დანარჩენი ფილმები (list): ", remaining_movies)


print("<3 პირველი ელემენტი: ", favorite_movies[0])
print("<3 ბოლო ელემენტი: ", favorite_movies[-1])
