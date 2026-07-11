# Simple Recommendation System
# Internship Task 4

movies = [
    {"name": "Inception", "genre": "Sci-Fi"},
    {"name": "Interstellar", "genre": "Sci-Fi"},
    {"name": "The Matrix", "genre": "Sci-Fi"},
    {"name": "Avengers: Endgame", "genre": "Action"},
    {"name": "John Wick", "genre": "Action"},
    {"name": "Spider-Man: No Way Home", "genre": "Action"},
    {"name": "The Conjuring", "genre": "Horror"},
    {"name": "Insidious", "genre": "Horror"},
    {"name": "The Nun", "genre": "Horror"},
    {"name": "3 Idiots", "genre": "Comedy"},
    {"name": "Jumanji", "genre": "Comedy"},
    {"name": "Home Alone", "genre": "Comedy"}
]

print("========== Movie Recommendation System ==========")
print("Available Genres:")
print("Sci-Fi | Action | Horror | Comedy")

genre = input("\nEnter your favorite genre: ").title()

recommendations = []

for movie in movies:
    if movie["genre"] == genre:
        recommendations.append(movie["name"])

if recommendations:
    print("\nRecommended Movies for You:")
    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")
else:
    print("\nSorry! No recommendations found for that genre.")