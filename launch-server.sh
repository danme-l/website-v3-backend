#!/bin/bash

# Activate the virtual environment
source server-env/Scripts/activate

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Run the Flask app
flask --app app.py run --debug
