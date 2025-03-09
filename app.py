from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to fetch a random Wikipedia article
def get_random_wikipedia_article():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h1", id="firstHeading").text
        return {"title": title, "link": response.url}
    else:
        return {"title": "Wikipedia is not accessible!", "link": "#"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_article")
def get_article():
    return jsonify(get_random_wikipedia_article())

if __name__ == "__main__":
    app.run(debug=True)
