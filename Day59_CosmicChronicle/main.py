from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_URL = "https://api.npoint.io/5ed94bd3afcdd77d5c65"
response = requests.get(url=BLOG_URL)
response.raise_for_status()
posts = response.json()

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def get_blog(index):
    requested_blog = None
    for post in posts:
        if post["id"] == index:
            requested_blog = post
            break
    if requested_blog:
        return render_template("post.html", post=requested_blog)
    else:
        return "<h1>Post not found</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)
