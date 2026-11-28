
from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "image": "https://placehold.co/300x200?text=Laptop"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 25000,
        "image": "https://placehold.co/300x200?text=Phone"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2000,
        "image": "https://placehold.co/300x200?text=Headphones"
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 3500,
        "image": "https://placehold.co/300x200?text=Watch"
    }
]


@app.route("/")
def home():
    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
