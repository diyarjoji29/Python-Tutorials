import spacy

# 1. Load spaCy’s English model
nlp = spacy.load("en_core_web_sm")

# 2. Process the text
text = "Apple is looking at buying U.K. startup for $1 billion. The deal was finalized in September, and everyone was excited about the acquisition."
doc = nlp(text)

# 🔹 Tokenization
tokens = [token.text for token in doc]
print("Tokens:")
print(tokens)

# 🔹 Remove Stop Words
filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
print("\nTokens without stop words:")
print(filtered_tokens)

# 🔹 Lemmatization
print("\nLemmatization (Original -> Lemma):")
for token in doc:
    print(f"{token.text} -> {token.lemma_}")
