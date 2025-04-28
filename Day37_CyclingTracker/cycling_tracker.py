import requests
from datetime import datetime

# ------------------------------- #
# User and Authentication Details
# ------------------------------- #
USERNAME = "your-username"  # Replace with your Pixela username
TOKEN = "your-token"        # Replace with your Pixela token

# ------------------------------- #
# Pixela API Endpoints
# ------------------------------- #
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# ------------------------------- #
# (Optional) Create a New User
# Only run once when setting up
# ------------------------------- #
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Uncomment below to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print("Create User Response:", response.text)

# ------------------------------- #
# (Optional) Create a New Graph
# Only run once when setting up
# ------------------------------- #
graph_params = {
    "id": "graph1",
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
# Uncomment below to create graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print("Create Graph Response:", response.text)

# ------------------------------- #
# Get Today's Date
# ------------------------------- #
today = datetime.now()
today_date = today.strftime("%Y%m%d")

# ------------------------------- #
# Ask User What to Do
# ------------------------------- #
print("\nWhat do you want to do today?")
print("1. Add/Update today's pixel")
print("2. View today's pixel data")
choice = input("Enter 1 or 2: ")

# ------------------------------- #
# Option 1: Add/Update Today's Pixel
# ------------------------------- #
if choice == "1":
    quantity_today = input("How many kilometers did you cycle today? ")

    pixel_params = {
        "date": today_date,
        "quantity": quantity_today
    }

    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

    if response.status_code == 409:  # Pixel already exists
        print("Pixel already exists. Updating today's entry...")
        pixel_update_endpoint = f"{pixel_endpoint}/{today_date}"
        response = requests.put(url=pixel_update_endpoint, json=pixel_params, headers=headers)

    print(response.text)

# ------------------------------- #
# Option 2: View Today's Pixel Data
# ------------------------------- #
elif choice == "2":
    pixel_view_endpoint = f"{pixel_endpoint}/{today_date}"

    response = requests.get(url=pixel_view_endpoint, headers=headers)

    if response.status_code == 200:
        pixel_data = response.json()
        quantity = pixel_data.get("quantity", "N/A")
        print(f"Today's cycling record: {quantity} km 🚴")
    else:
        print("No data found for today or an error occurred.")
        print(response.text)

# ------------------------------- #
# Invalid Choice Handling
# ------------------------------- #
else:
    print("Invalid choice. Please run the script again and enter 1 or 2.")
