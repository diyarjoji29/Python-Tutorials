import nltk
import pandas as pd
import random
import string
from nltk.corpus import movie_reviews, stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 🔽 Download required datasets (runs only once)
nltk.download('movie_reviews')
nltk.download('stopwords')

# 🔹 Load movie review data
documents = [(movie_reviews.raw(fileid), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
df = pd.DataFrame(documents, columns=['review_text', 'label'])

# 🔹 Preprocess: lowercase, remove punctuation and stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

df['cleaned_text'] = df['review_text'].apply(clean_text)

# 🔹 Bag of Words (Top 50)
vectorizer = CountVectorizer(max_features=50)
bow_matrix = vectorizer.fit_transform(df['cleaned_text'])
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# 🔹 Show top 10 BoW words
top_words = bow_df.sum().sort_values(ascending=False)
print("\nTop 10 frequent words (BoW):")
print(top_words.head(10))

# 🔹 TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=50)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['cleaned_text'])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

print("\nTop 5 TF-IDF words from first review:")
print(tfidf_df.iloc[0].sort_values(ascending=False).head(5))

# 🔹 Bar Chart
top_words.head(10).plot(kind='barh', title='Top 10 Frequent Words (BoW)')
plt.gca().invert_yaxis()
plt.show()

# 🔹 Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['cleaned_text']))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
