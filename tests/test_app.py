
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app import app


def test_home_page():
    app.config["TESTING"] = True

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_website_title():
    client = app.test_client()

    response = client.get("/")

    assert b"E-commerce Store" in response.data


def test_products_display():
    client = app.test_client()

    response = client.get("/")

    assert b"Laptop" in response.data
    assert b"Smartphone" in response.data

