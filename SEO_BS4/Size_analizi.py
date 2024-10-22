import requests
from bs4 import BeautifulSoup

def size_analizi(url_link):
    response = requests.get(url_link)

    soup = BeautifulSoup(response.text, 'html.parser')

    page_size_bytes = len(response.content)
    page_size_kb = page_size_bytes / 1024

    print(f"Page size: {page_size_bytes} bayt")
    if page_size_kb >= 500:
        print(f"Page size bigger than the rocomended size! ({round(page_size_kb,2)})")
    else:
        print(f"Page size is good: ({round(page_size_kb,2)} kb)")