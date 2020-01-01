from flask import Flask
import feedparser

app = Flask(__name__)
URL_RSS = 'https://www.kaldata.com/софтуер/feed'


@app.route('/')
def index():
    parser = feedparser.parse(URL_RSS)
    first_arcticle = parser
    return f"{first_arcticle}"


if __name__ == '__main__':
    app.run(debug=True)
