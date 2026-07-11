# Simple Recommendation System

movies = {
    "Action": [
        "John Wick",
        "Avengers",
        "Mad Max"
    ],
    "Comedy": [
        "3 Idiots",
        "The Mask",
        "Home Alone"
    ],
    "Horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle"
    ],
    "Sci-Fi": [
        "Interstellar",
        "Inception",
        "The Matrix"
    ],
    "Romance": [
        "Titanic",
        "La La Land",
        "The Notebook"
    ]
}

print("===== Movie Recommendation System =====")
print("Available Categories:")

for category in movies:
    print("-", category)

choice = input("\nEnter your favorite category: ").title()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("•", movie)
else:
    print("\nSorry! Category not available.")