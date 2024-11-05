#!/usr/bin/env python3
"""flask server"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    # Class attribute for available language
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """home route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(port=1111, debug=True)
