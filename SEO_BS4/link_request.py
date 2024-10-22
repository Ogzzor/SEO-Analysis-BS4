import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import matplotlib.pyplot as plt
from colorama import Fore
#from fontTools.misc.cython import returns

def link_req(url_link):
    response = requests.get(url_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    base_url = urlparse(url_link).netloc

    internal_links = []
    external_links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            full_url = urljoin(url_link, href)
            parsed_url = urlparse(full_url)
            if parsed_url.netloc == base_url:
                internal_links.append(full_url)
            else:
                external_links.append(full_url)

    all_links = internal_links + external_links

    print(f"All links count: {len(all_links)}")
    print(f"Internal links count: {len(internal_links)}")
    if len(internal_links) >= 11:
        print(Fore.RED + f"According to Google standart internal links to much! Maksimum 10 links -> {len(internal_links)}")
    elif len(internal_links) <= 2:
        print(Fore.RED + f"According to Google standart internal links number are low! Minimum 3 links -> {len(internal_links)}")
    else:
        print(Fore.RESET +"Internal links number are fine")
    print(f"External links count: {len(external_links)}")
    if len(external_links) >= 3:
        print(Fore.RED + f"According to Google standart external links to much! Maksimum 3 links -> {len(external_links)}")
    elif len(internal_links) <= 0:
        print(Fore.RED + f"According to Google standart external links number are low! Minimum 1 links -> {len(external_links)}")
    else:
        print(Fore.RESET +"External links number are fine")
    print(Fore.RESET + " ")
    # print("External Links:")
    # for i in external_links:
    #     print(i)

    pie_eleman = [len(internal_links), len(external_links)]
    pie_labels = ["Internal links", "External links"]
    plt.pie(pie_eleman, labels=pie_labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Link Analysis Pie Chart\n"
    f"Total: {len(all_links)}, Internal: {len(internal_links)}, External: {len(external_links)}")
    plt.show()


    # sinyal = []
    # broken = []
    #
    # for b in all_links:
    #     try:
    #         response = requests.get(b, timeout=10)  # Timeout added for slow or unreachable URLs
    #         sinyal.append(response)
    #     except requests.exceptions.RequestException as e:
    #         broken.append(b)
    #
    #     # Check the status codes of the responses
    #     for response in sinyal:
    #         if response.status_code >= 400:
    #             broken.append(response.url)  # Append broken link URL