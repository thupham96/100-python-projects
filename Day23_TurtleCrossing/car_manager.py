from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_START_X = 300
CAR_LIMIT_X = -320  # Cars will be removed when they move past this point
LANE_SPACING = 20  # Space cars into lanes for better distribution


class CarManager:
    def __init__(self):
        """Manages the cars in the game, including creation, movement, and speed increase."""
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a new car and adds it to the list of moving cars."""
        new_car = Turtle()
        new_car.shape("square")
        new_car.turtlesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()

        # Randomize car position within lanes to avoid overlap
        y_position = random.randint(-250, 250) // LANE_SPACING * LANE_SPACING
        new_car.goto(CAR_START_X, y_position)
        new_car.setheading(180)  # Move left

        self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars forward and removes those that exit the screen."""
        for car in self.all_cars:
            car.forward(self.speed)

        # Remove cars that have moved off-screen
        self.all_cars = [car for car in self.all_cars if car.xcor() > CAR_LIMIT_X]

    def increase_speed(self):
        """Increases the speed of all cars."""
        self.speed += MOVE_INCREMENT
