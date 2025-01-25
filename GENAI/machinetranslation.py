from translate import Translator

translator = Translator(to_lang='es')  # Spanish
# Text to be translated
text = 'Where are you from?'
# Perform the translation
translation = translator.translate(text)

# Print the translated text
print('Translated Text:', translation)