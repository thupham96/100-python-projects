from flask import Flask, render_template, request
import requests

app = Flask(__name__)
BLOG_URL = "https://api.npoint.io/d10342d51c20d4b0abb2"
response = requests.get(url=BLOG_URL)
response.raise_for_status()
posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:index>')
def get_blog(index):
    for post in posts:
        if post["id"] == index:
            requested_blog = post
    return render_template("post.html", post=post)

@app.route('/search')
def search():
    query = request.args.get("query", "").lower()
    filtered_posts = [post for post in posts if query in post["title"].lower() or query in post["subtitle"].lower()]
    return render_template("index.html", posts=filtered_posts)

if __name__ == "__main__":
    app.run(debug=True)
