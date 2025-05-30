# Day 59: 🌌 Cosmic Chronicle – Flask Blog Site 🚀📝

Create a responsive, themed blog site using **Flask**, **HTML**, **CSS**, and **Bootstrap**, pulling blog data from an external JSON API. This project combines frontend styling with backend routing to deliver a dynamic, user-friendly experience for cosmic storytelling.

## 🌠 Overview

**Cosmic Chronicle** is a space-inspired blog platform that showcases posts fetched from an external API. It features a homepage with previews, a full post view, and standard pages like About and Contact. The site is styled with a modern Bootstrap template to ensure responsiveness across devices.

## 🔭 Live Preview

```bash
flask run
```

Visit: `http://localhost:5000/`

## 🧩 Key Pages & Routes

| Route           | Description                         |
| --------------- | ----------------------------------- |
| `/`             | Home page listing all blog posts    |
| `/post/<id>`    | Detailed view of an individual post |
| `/about.html`   | About the author                    |
| `/contact.html` | Contact form (form styling only)    |

## 💡 Features

* 🔄 Dynamic content rendering with Flask & Jinja2
* 🌐 External blog data from [npoint.io JSON API](https://api.npoint.io/5ed94bd3afcdd77d5c65)
* 📄 Multiple HTML pages using `render_template` and includes (`header.html`, `footer.html`)
* ✍️ Custom author section: *The Cosmic Pen*
* 📱 Mobile-first Bootstrap 5 design
* 📩 Styled contact form (requires integration to be functional)

## 📂 Project Structure

```
Day59_CosmicChronicle/
├── main.py
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── about.html
│   ├── contact.html
│   ├── header.html
│   └── footer.html
├── static/
│   ├── assets/
│   │   └── img/
│   │       ├── home-bg.jpg
│   │       ├── about-bg.jpg
│   │       ├── contact-bg.jpg
│   │       └── post-bg.jpg
│   └── css/
│       └── styles.css
```

## 🛠️ How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day59_CosmicChronicle
   ```

2. **Install Flask:**

   ```bash
   pip install flask
   ```

3. **Run the App:**

   ```bash
   python main.py
   ```

4. **Open in Browser:**

   Visit `http://127.0.0.1:5000/`

## 🧰 Technologies Used

* Flask
* HTML5 + Jinja2 templating
* CSS3
* Bootstrap 5
* Font Awesome
* Google Fonts

## 🧠 What I Learned

* Building multi-page Flask applications
* Rendering external JSON content into templates
* Modularizing HTML with includes
* Styling with Bootstrap and responsive layout
* Connecting logic and design for blog platforms

---

✨ Dive into the universe one blog post at a time — powered by Python and passion.
