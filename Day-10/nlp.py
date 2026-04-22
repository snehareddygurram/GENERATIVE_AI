# Day-07/nlp.py

# Input sentence
text = "I am learning AI and it is powerful"

# Convert to lowercase
text = text.lower()

# Tokenization (split into words)
tokens = text.split()

print("Tokens:", tokens)

# Define stopwords
stopwords = ["am", "is", "and", "it"]

# Remove stopwords
filtered = [word for word in tokens if word not in stopwords]

print("Filtered words:", filtered)