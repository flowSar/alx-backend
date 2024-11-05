#!/usr/bin/env python3
"""flask server"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    # Class attribute for available language
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config.from_object(Config)


@app.route("/")
def home():
    """home route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port=1111, debug=True)
