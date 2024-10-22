import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def image_analizi(url_link):
    response = requests.get(url_link)

    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")

    img_description = []
    img_no_description = []

    for img in images:
        img_src = img.get("src")
        img_alt = img.get("alt", "")

        if img_alt == "":
            img_no_description.append(img_src)
        else:
            img_description.append(img_src)

    x = ["Image with description", "Image without description"]
    y = [len(img_description), len(img_no_description)]
    widths = [0.5, 0.5]
    colors = ["#00ba38", "#f8766d"]

    plt.bar(x = x, height = y, width = widths, color = colors)
    plt.title("Image Analysis")

    for i, v in enumerate(y):
        plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

    print(f"Total number of images: {len(images)}")
    print(f"Number of images with description: {len(img_description)}")
    print(f"Number of images without description: {len(img_no_description)}")
    plt.show()