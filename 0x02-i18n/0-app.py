#!/usr/bin/env python3
"""flask server"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    """home route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port=1111, debug=True)
