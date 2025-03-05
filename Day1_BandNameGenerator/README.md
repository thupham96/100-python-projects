# Day 1: Band Name Generator

Welcome to the Band Name Generator! This project is a fun way to create unique band names based on user inputs, such as the city they grew up in, their pet’s name, and their preferred music genre.

## How It Works

1. The program asks for the user’s city of origin.
2. It then asks for the name of their pet.
3. Finally, the user selects a genre for their band.
4. Based on the genre, a unique band name is generated using predefined naming patterns.

## Band Name Rules

- **Rock**: Follows the format *The {City} {Pet}s* (e.g., *The New York Tigers*).
- **Jazz**: Follows the format *{Pet} & The {City} Groove* (e.g., *Max & The Paris Groove*).
- **Metal**: Follows the format *{City} {Pet} of Doom* (e.g., *London Shadow of Doom*).
- **Other Genres**: Uses a simple format *{City} {Pet}* (e.g., *Chicago Echo*).

### Example Run:
```plaintext
Welcome to the Band Name Generator.
Which city did you grow up in?
> Seattle
What is the name of your pet?
> Luna
What genre does your band play? (rock, jazz, pop, metal, etc.)
> rock
Your rock band name: The Seattle Lunas
```

## Features

- **Custom Genre-Based Names**: Generates different styles of band names based on the chosen genre.
- **User Interaction**: Takes user inputs dynamically.
- **Simple and Fun**: A beginner-friendly introduction to Python’s `input()` function and string manipulation.

## How to Use

1. Clone the repository and navigate to the `Day1_BandNameGenerator` folder:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day1_BandNameGenerator
   ```
2. Run the script:
   ```bash
   python band_name_generator.py
   ```
3. Follow the on-screen prompts to generate your band name!

## Technologies Used

- Python 3
- String manipulation for name formatting
- User input handling

## What I Learned

- Taking user input using `input()`.
- Using conditional statements to generate different outputs.
- Formatting strings dynamically for varied results.

Enjoy generating cool band names and rock on! 🎸🎶
