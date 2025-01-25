from textblob import TextBlob
text = 'I love progamming and machine learnig.'
blob = TextBlob(text)
corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)
