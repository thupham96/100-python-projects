# Day 66: ☕ Cafe & Wifi API – Flask + SQLAlchemy 🔌📶

A Flask-based RESTful API to manage a collection of cafes and their amenities (like Wi-Fi, power sockets, toilets, coffee price, etc.). This project uses SQLAlchemy with a SQLite database and supports full CRUD operations via HTTP routes.

---

## 📖 Overview

**Cafe & Wifi API** lets users:

* Retrieve random or all cafes from the database
* Search cafes by location
* Add new cafes with details
* Update coffee prices
* Delete cafes (with API key authentication)

---

## 🚀 Run the App

```bash
python main.py
```

Visit the app:

```
http://127.0.0.1:5000/
```

---

## 📁 Setup Instructions

1. **Clone the repository or copy the files:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day66_CafeWifiAPI
   ```

2. **Install the required packages:**

   ```bash
   pip install flask flask_sqlalchemy
   ```

3. **Run the application:**

   ```bash
   python main.py
   ```

---

## 🗺️ API Endpoints

| Method | Route                                         | Description                            |
| ------ | --------------------------------------------- | -------------------------------------- |
| GET    | `/`                                           | Homepage (HTML template)               |
| GET    | `/random`                                     | Returns one random cafe                |
| GET    | `/all`                                        | Returns all cafes                      |
| GET    | `/search?loc=<location>`                      | Searches cafes by location             |
| POST   | `/add`                                        | Adds a new cafe (form data required)   |
| PATCH  | `/update/<id>?new_price=<price>`              | Updates coffee price for a cafe by ID  |
| DELETE | `/report-closed/<id>?api-key=TopSecretAPIKey` | Deletes cafe with API key (admin only) |

---

## 🧾 Cafe Model Fields

```python
id
name
map_url
img_url
location
seats
has_toilet
has_wifi
has_sockets
can_take_calls
coffee_price
```

---

## 💡 Features

* 📍 Search by location with partial match
* 🆕 Add new cafes via form-data
* 🔄 Update prices with PATCH
* 🔐 Secure delete with simple API key
* 📄 JSON responses for all API calls
* 🛠️ Built using Flask + SQLAlchemy

---

## 🔐 API Notes

* Deleting a cafe requires the API key `TopSecretAPIKey` as a query param.
* POST data must be sent as `application/x-www-form-urlencoded`.

---

## 🧠 What I Learned

* Creating RESTful APIs using Flask
* Modeling databases with SQLAlchemy and SQLite
* Handling CRUD routes and validating request data
* Error handling and secure route access
* Building flexible, testable web APIs

---

☕ Explore digital nomad-friendly cafes with this simple yet powerful Flask API — or integrate it into your next app or web dashboard!
