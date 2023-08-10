#!/bin/bash

# initializing for coding sessions

# activate the virtual environment
source server-env/Scripts/activate

# set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# run the Flask app
flask --app app.py run --debug
