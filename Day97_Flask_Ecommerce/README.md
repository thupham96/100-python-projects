# Day 97: Flask E-Commerce – Simple Storefront with Cart

A minimal yet fully functional e-commerce web application built with **Flask** and **SQLite**. This app allows users to browse products, add items to a cart, update quantities, and review totals—all with clean UI and stateful session storage.

---

## Features

* Browse all available products on a responsive product grid
* Add items to a shopping cart (with session-based storage)
* Update item quantities or remove items from the cart
* "Clear Cart" and placeholder "Checkout" actions
* Automatically seeded sample products on first launch
* Jinja2-based templates with cart badge updates
* Price formatting via Flask template filters

---

## Technologies Used

* **Python 3**
* **Flask** – Web framework
* **Flask-SQLAlchemy** – ORM with SQLite
* **HTML + Jinja2** – Dynamic templates
* **Bootstrap or custom CSS** (add your own for styling)

---

## Project Structure

```
.
├── app.py               # Main Flask app
├── templates/
│   ├── products.html    # Displays product catalog
│   └── cart.html        # Shows items in cart
└── static/              # (Optional) Add CSS, JS, image assets
```

---

## How to Run

1. **Install dependencies:**

   ```bash
   pip install flask flask_sqlalchemy
   ```

2. **Clone the project:**

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day97_Flask_Ecommerce
   ```

3. **Run the app:**

   ```bash
   python app.py
   ```

4. **Visit in browser:**

   ```
   http://127.0.0.1:5000/
   ```

---

## How It Works

* The app uses `Flask-SQLAlchemy` to model `Product` data and store it in `store.db`.
* Sample products are auto-seeded into the database on first run.
* Cart data is stored in Flask session using a dictionary (`{product_id: qty}`).
* Each template displays a dynamic cart badge showing current cart count.
* Cart items can be updated, removed, or cleared entirely.

---

## UI Highlights

### Product Page (`products.html`)

* Shows product image, name, price, description, and stock.
* "Add to Cart" button disabled when stock is 0.

### Cart Page (`cart.html`)

* Displays line-item totals and overall cart total
* Input to update quantity or remove individual items
* "Clear Cart" and placeholder "Check out" buttons

---

## What I Learned

* Building multi-page Flask apps with routing and state (sessions)
* Using SQLAlchemy to define models and seed data
* Structuring a simple but scalable Flask project
* Writing modular HTML with Jinja2 templating
* Implementing cart logic and syncing UI with server data
* Formatting prices using custom Flask filters

---

## Future Improvements

* Add user accounts and authentication
* Integrate payment gateway or dummy checkout flow
* Real-time stock update and quantity validation
* Use SQLite for persistent cart if login is added

Let me know if you'd like me to export this as a file or include it in your GitHub project folder!
