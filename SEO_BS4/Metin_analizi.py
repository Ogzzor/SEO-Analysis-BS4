import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import matplotlib.pyplot as plt

def metin_analizi(url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    words = re.findall(r'\b[a-zA-ZğüşıöçĞÜŞİÖÇ]+\b', cleaned_text.lower())

    word_counts = Counter(words)
    most_common_words = word_counts.most_common(20)
    total_characters = len(cleaned_text)
    total_words = len(words)

    words, counts = zip(*most_common_words)
    plt.bar(words, counts, color= "green")
    plt.xlabel("Words")
    plt.ylabel("Counts")
    plt.title("Most Used 10 words")
    plt.xticks(rotation=45)

    for i, v in enumerate(counts):
        plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

    print(f"Total number of characters: {total_characters}")
    print(f"Total number of words: {total_words}")
    #print("Most used 10 words:")
    #for word, count in most_common_words:
        #print(f"{word} used {count} times")
    plt.show()