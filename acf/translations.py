_translations = {
    'content': {
        'register_feedback_message': {
            'en': "Register feedback here.",
            'no': "Registrer tilbakemelding her."
        }
    }
}


class Translator:

    def __init__(self, language_code='en', fallback_language_code='en'):
        self.language_code = language_code
        self.fallback_language_code = fallback_language_code

    def get_translation(self, translation_code):
        translation_node = _translations
        for code in translation_code.split('.'):
            translation_node = translation_node[code]

        try:
            return translation_node[self.language_code]
        except ValueError:
            return translation_node[self.fallback_language_code]
