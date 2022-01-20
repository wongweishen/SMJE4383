#Natural Language Processing & Sentiment Analysis
#1. pip install textblob

from textblob import TextBlob
text = 'Tomorrow will be a great weekend for us'
blob = TextBlob(text)
blob.detect_language()
chinese = blob.translate(to='zh')
spanish = blob.translate(to='es')
#Polarity: -1.0 (Negative) to 1.0 (Positivi)
#Subjectivity : 0.0 (Objective) to 1.0 (Subjective)
blob.sentiment

text1 = 'Yesterday was a beautiful day, but today looks like bad weather'
blob1 = TextBlob(text1)
blob1.sentiment
print(chinese)
