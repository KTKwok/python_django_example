from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    val = random.randint(1, 10)
    return render_template("index.html", name=val)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

if __name__ == '__main__':
    app.run(debug=True)