from flask import Flask, render_template, request
import requests
import smtplib

# Email, password and api_key
my_email = "<your-email>"
my_password = "<your-email-password>"
to_email = "<recipient-email>"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    else:
        email_body = f"Name: {request.form["name"]}\nEmail: {request.form["email"]}\nPhone: {request.form["phone"]}\nMessage: {request.form["message"]}"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:New Message!\n\n{email_body}"
            )
            print(f"Email sent!")
        return render_template("contact.html", msg_sent=True)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
