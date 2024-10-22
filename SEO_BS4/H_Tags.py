import requests
from bs4 import BeautifulSoup
from colorama import Fore
import matplotlib.pyplot as plt
import os

def h_tags (url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, "lxml")

    h1 = []
    h2 = []
    h3 = []
    h4 = []
    h5 = []
    h6 = []

    heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]

    for tag in heading_tags:
        for tags in soup.find_all(tag):
            if tags.name == "h1":
                h1.append(tags.text.strip())
            elif tags.name == "h2":
                h2.append(tags.text.strip())
            elif tags.name == "h3":
                h3.append(tags.text.strip())
            elif tags.name == "h4":
                h4.append(tags.text.strip())
            elif tags.name == "h5":
                h5.append(tags.text.strip())
            else:
                h6.append(tags.text.strip())

    if h1:
        print(Fore.GREEN + f"h1 available -> {h1}")
    else:
        print(Fore.RED + "h1 not available!!!!")

    print(Fore.RESET + f"h2 count: {len(h2)}")
    print(f"h3 count: {len(h3)}")
    print(f"h4 count: {len(h4)}")
    print(f"h5 count: {len(h5)}")
    print(f"h6 count: {len(h6)}")

    all_counts = [len(h1), len(h2), len(h3), len(h4), len(h5), len(h6)]
    filtered_counts = [count for count in all_counts if count > 0]
    filtered_labels = [label for count, label in zip(all_counts, heading_tags) if count > 0]

    plt.pie(filtered_counts, labels=filtered_labels, startangle=90,
            autopct=lambda p: f'{p:.1f}%\n({int(p*sum(filtered_counts)/100)})',
            pctdistance=1.25, labeldistance=.6)

    plt.title("H Tags Chart")
    plt.legend(title="Tags Colors:")
    plt.show()