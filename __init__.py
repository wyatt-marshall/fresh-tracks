#! /usr/bin/env python3

import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        DATABASE=os.path.join(app.instance_path, 'flask

@app.route("/")
def 
