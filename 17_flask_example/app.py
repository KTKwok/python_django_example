from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    val = random.randint(1,10)
    return render_template("index.html", name=val)

if __name__ == '__main__':
    app.run(debug=True)