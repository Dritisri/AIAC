import string
from collections import Counter

def most_frequent_word(paragraph):
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequencies
    freq = Counter(words)
    # Find the most common word
    if freq:
        return freq.most_common(1)[0][0]
    else:
        return None