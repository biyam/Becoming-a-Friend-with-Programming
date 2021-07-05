'''1. import nltk
2. nltk.download('punkt')
3. nltk.download('averaged_perceptron_tagger')'''


from nltk.tokenize import word_tokenize
text = "I love you"
print('=>', text); print()
print('=>', word_tokenize(text)); print()
from nltk.tag import pos_tag
x = word_tokenize(text)
print('=>', pos_tag(x))
