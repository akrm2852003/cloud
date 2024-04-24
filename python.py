import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
# Get the English stop words list from NLTK
stop_words = set(stopwords.words('english'))

def remove_stop_words(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    # Remove stop words from the text
    filter_words = [word for word in words if word.lower() not in stop_words]
    return filter_words

def count_word_occurrences(words):
    # Count the occurrences of each word in the list
    counts = Counter(words)
    return counts
with open("random_paragraphs.txt", "r") as file:
    text = file.read()
filter_words = remove_stop_words(text)
counts = count_word_occurrences(filter_words)

# Display the remaining words and their counts side by side
for word, count in counts.items():
    print(f"{word}: {count}")