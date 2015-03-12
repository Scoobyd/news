from textblob import TextBlob

text = str('More and more information from local, state and federal governments is being placed on the web.')

blob = TextBlob(text)

print blob.polarity
# 0.060
# -0.341