import requests
import time
def load_time(url_link):
    start_time = time.time()
    response = requests.get(url_link)
    end_time = time.time()

    loading_time = end_time - start_time

    print(f"The loading time for {url_link} is {loading_time*1000} milliseconds.")