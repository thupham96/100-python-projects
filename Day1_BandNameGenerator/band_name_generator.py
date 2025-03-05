# Welcome message for the Band Name Generator
print("Welcome to the Band Name Generator.")

# Ask the user for the city they grew up in
city = input("Which city did you grow up in?\n")

# Ask the user for their pet's name
pet = input("What is the name of your pet?\n")

# Ask the user for the genre of their band and convert it to lowercase for case-insensitive comparison
genre = input("What genre does your band play? (rock, jazz, pop, metal, etc.)\n").lower()

# Generate the band name based on the selected genre
if genre == "rock":
    # Rock band names follow the format: "The {city} {pet}s"
    print(f"Your rock band name: The {city} {pet}s")
elif genre == "jazz":
    # Jazz band names follow the format: "{pet} & The {city} Groove"
    print(f"Your jazz band name: {pet} & The {city} Groove")
elif genre == "metal":
    # Metal band names follow the format: "{city} {pet} of Doom"
    print(f"Your metal band name: {city} {pet} of Doom")
else:
    # Default band name format if the genre is not specified
    print(f"Your band name: {city} {pet}")
