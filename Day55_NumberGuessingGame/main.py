from flask import Flask
import random

app = Flask(__name__)

# Generate a random number only once when the server starts
random_number = random.randint(0, 100)
guess_count = 0

@app.route("/")
def guess_a_number():
    return ('<h1>Guess a number between 0 and 100</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:number>")
def check_if_number_is_correct(number):
    global guess_count
    guess_count += 1
    if number < random_number:
        return (f'<h1 style="color: red;">Too low, try again!</h1>'
                f'<p>Guesses: {guess_count}</p>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2todTUybHkzYXcxYzhqODYwNmc5MXhuNHZhemJhNG9ocWU0N3JsYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohc17IuNgUpALSaIM/giphy.gif">')
    elif number > random_number:
        return (f'<h1 style="color: purple;">Too high, try again!</h1>'
                f'<p>Guesses: {guess_count}</p>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return (f'<h1 style="color: green;">You found me!</h1>'
                f'<p>Guesses: {guess_count}</p>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

@app.route("/reset")
def reset_game():
    global random_number
    random_number = random.randint(0, 100)
    return "<h3>Game reset! Guess a new number between 0 and 100.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
