import os
from flask import Flask
from flask import render_template

from acf.translations import Translator

app = Flask(__name__)
app.config['DEBUG'] = is_debug = os.environ.get('APP_ENV', 'production') == 'debug'

app_title = os.environ.get('APP_TITLE', 'Apartment Complex Feedback')
language_code = os.environ.get('APP_LANGUAGE_CODE', 'en')

translator = Translator(language_code)


@app.route('/')
def main():
    return render_template(
        'main.html',
        page_title=app_title
    )


@app.template_filter('translate')
def translate(translation_code):
    return translator.get_translation(translation_code)
