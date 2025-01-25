from translate import Translator

translator = Translator(to_lang='es')  #Spanish
# Text to be translated
text = 'Where are you from?'
# Performs the translation
translation = translator.translate(text)

# Prints the translated text
print('Translated Text:', translation)
