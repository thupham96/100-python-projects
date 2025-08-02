from flask import Flask, request, render_template
import os
import requests

URL = "https://api.languagetool.org/v2/check"

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

def apply_corrections(text, matches):
    matches = sorted(matches, key=lambda m: m["offset"], reverse=True)

    for match in matches:
        if match["replacements"]:
            start = match["offset"]
            end = start + match["length"]
            replacement = match["replacements"][0]["value"]
            text = text[:start] + replacement + text[end:]
    return text

@app.route("/grammar", methods=["GET", "POST"])
def grammar_check():
    if request.method == "POST":
        text = request.form.get("text")

        data = {
            "text": text,
            "language": "en-US"
        }

        response = requests.post(URL, data=data)

        if response.status_code == 200:
            result = response.json()
            suggestions = []
            for match in result["matches"]:
                suggestions.append({
                    "message": match["message"],
                    "offset": match["offset"],
                    "length": match["length"],
                    "suggestions": [s["value"] for s in match["replacements"]]
                })
            corrected_text = apply_corrections(text, result["matches"])
            return render_template("result.html", original=text, suggestions=suggestions,
                                   corrected_text=corrected_text)
        else:
            error = f"Error {response.status_code}: {response.text}"
            return render_template("index.html", error=error)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
