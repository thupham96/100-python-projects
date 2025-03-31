import requests

CATEGORIES = {
    "Any": None,
    "General Knowledge": 9,
    "Books": 10,
    "Film": 11,
    "Music": 12,
    "Musicals & Theatres": 13,
    "Television": 14,
    "Video Games": 15,
    "Board Games": 16,
    "Science & Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "Mythology": 20,
    "History": 23,
    "Sports": 21,
    "Geography": 22,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27
}

DIFFICULTIES = ["Any", "easy", "medium", "hard"]

def fetch_questions(amount=10, category=None, difficulty=None):
    params = {
        "amount": amount,
        "type": "boolean"
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    print(params)
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    print(response.json()["results"])
    return response.json()["results"]
