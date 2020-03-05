import os
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = is_debug = os.environ.get('APP_ENV', 'production') == 'debug'


@app.route('/')
def hello():
    return "Hello World!"
