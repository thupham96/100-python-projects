from flask import Flask, render_template, session, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "dev-secret-change-me"

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    price_cents = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.Text, nullable=True)
    stock = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Product {self.name}"

@app.template_filter("currency")
def currency_cents(cents: int) -> str:
    try:
        return f"${cents/100:,.2f}"
    except Exception:
        return "$0.00"

@app.route("/")
@app.route("/products")
def list_products():
    products = Product.query.order_by(Product.id.asc()).all()
    return render_template("products.html", products=products, cart_item_count=cart_count())

def seed_if_empty():
    if Product.query.first():
        return
    sample_products = [
        {
            "name": "Classic Mug",
            "price_cents": 1299,
            "img_url": "https://cdn.commercev3.net/cdn.benningtonpotters.com/images/uploads/9925-american-classic-mug-w-pop.jpg",
            "description": "Sturdy ceramic mug for your daily brew.",
            "stock": 42
         },
        {
            "name": "Cotton T-Shirt",
            "price_cents": 1999,
            "img_url": "https://allmade.com/cdn/shop/files/unisex-organic-cotton-tee-155122_900x.jpg?v=1749741363",
            "description": "Soft, breathable cotton tee. Unisex fit.",
            "stock": 30
        },
        {
            "name": "Canvas Tote",
            "price_cents": 2499,
            "img_url": "https://m.media-amazon.com/images/I/81gt+tL77NL.jpg",
            "description": "Reusable tote bag with reinforced handles.",
            "stock": 18
        },
        {
            "name": "Leather Journal",
            "price_cents": 2450,
            "img_url": "https://www.colonellittleton.com/wp-content/uploads/2019/07/journal-no9-lifestyle-scaled.webp",
            "description": "Hand-stitched vegan-leather cover with 120 pages of thick, bleed-resistant paper. Great for sketching and daily notes.",
            "stock": 20
        },
        {
            "name": "Enamel Camping Mug",
            "price_cents": 1499,
            "img_url": "https://www.spiriteddesignstudio.com/cdn/shop/products/92793dace632ef9428e9710e80663375.jpg?v=1680291049&width=1946",
            "description": "Lightweight enamel-coated steel mug with a vintage speckle finish. Perfect for campfires or morning coffee on the porch.",
            "stock": 36
        },
        {
            "name": "Leather Notebook",
            "price_cents": 1599,
            "img_url": "https://m.media-amazon.com/images/I/71KrzFrUWHL.jpg",
            "description": "A5 dotted journal with a soft leather cover and 160 pages.",
            "stock": 25,
        },
        {
            "name": "Insulated Water Bottle",
            "price_cents": 2899,
            "img_url": "https://m.media-amazon.com/images/I/717yvDavBlL._UF894,1000_QL80_.jpg",
            "description": "Double-wall stainless steel bottle that keeps drinks cold for 24h.",
            "stock": 0
        }
    ]
    for p in sample_products:
        db.session.add(Product(**p))
    db.session.commit()


# --- Cart helpers ---
def get_cart() -> dict:
    cart = session.get("cart")
    if not isinstance(cart, dict):
        cart = {}
    return cart

def save_cart(cart: dict):
    session["cart"] = cart
    session.modified = True

def cart_count(cart: dict | None=None) -> int:
    cart = cart if cart is not None else get_cart()
    return sum(cart.values())

@app.context_processor
def inject_cart_badge():
    return {"cart_item_count": cart_count()}

# --- Cart routes ---
@app.post("/cart/add/<int:product_id>")
def cart_add(product_id: int):
    cart = get_cart()
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    save_cart(cart)
    flash("Added to cart.", "success")
    return redirect(request.referrer or url_for("list_products"))

@app.get("/cart")
def view_cart():
    cart = get_cart()
    if not cart:
        items = []
        total_cents = 0
    else:
        ids = [int(pid) for pid in cart.keys()]
        products = Product.query.filter(Product.id.in_(ids)).all()
        items = []
        total_cents = 0
        by_id = {p.id: p for p in products}
        for pid_str, qty in cart.items():
            pid = int(pid_str)
            p = by_id.get(pid)
            if p:
                line_total = p.price_cents * qty
                total_cents += line_total
                items.append({'product': p, 'qty': qty, 'line_total':line_total})
                print(p.img_url)
    return render_template("cart.html", items=items, total_cents=total_cents)

@app.post("/cart/update/<int:product_id>")
def cart_update(product_id: int):
    qty = request.form.get("qty", type=int)
    cart = get_cart()
    key = str(product_id)
    cart[key] = qty
    save_cart(cart)
    return redirect(url_for("view_cart"))

@app.post("/cart/remove/<int:product_id>")
def cart_remove(product_id: int):
    cart = get_cart()
    if cart:
        del cart[str(product_id)]
        save_cart(cart)
    return redirect(url_for("view_cart"))

@app.post("/cart/clear")
def cart_clear():
    save_cart({})
    return redirect(url_for("view_cart"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_if_empty()
    app.run(debug=True)