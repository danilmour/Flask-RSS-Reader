from flask import Flask, render_template
import feedparser

# Create Database File
# from app import db
# db.create_all()

app = Flask(__name__)


@app.route("/")
def index():
    jornais = ["Jornal de Notícias", "Pplware"]

    return render_template("index.html", jornais=jornais)


@app.route("/jn")
def jn():
    rss = feedparser.parse("http://feeds.jn.pt/JN-Ultimas")

    return render_template("rss.html", rss=rss)


@app.route("/pplware")
def pplware():
    rss = feedparser.parse("https://pplware.sapo.pt/feed/")

    return render_template("rss.html", rss=rss)


if __name__ == "__main__":
    app.run(debug=True)
