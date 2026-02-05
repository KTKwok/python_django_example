from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=current_time)

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        products = [
            {"sku":"Apple", "price":10},
            {"sku": "Banana", "price": 20},
            {"sku": "Cherry", "price": 14},
            {"sku": "Pear", "price": 12},
        ]
        return render_template("about.html", products=products)

    # Post Action
    cust_email = request.form["cust_email"]
    cust_email = cust_email.split("@")
    return render_template("thankyou.html", prefix=cust_email[0], domain=cust_email[1])

@app.route("/calculate_csv", methods=["GET", "POST"])
def calculate_csv():
    if request.method == "POST":
        if 'files' not in request.files:
            return "No file"

        files = request.files.getlist("files")

        dataframes = []
        for f in files:
            df = pd.read_csv(f)

            df['total'] = df['qty'] * df['cost']
            dataframes.append(df)

        combined_df = pd.concat(dataframes, ignore_index=True)

        table_html = combined_df.to_html(classes="table", index=False)

        return render_template("csv_result.html", table=table_html)

    return render_template("calculate_csv.html")

if __name__ == '__main__':
    app.run(debug=True)