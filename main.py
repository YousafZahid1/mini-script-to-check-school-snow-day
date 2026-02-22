import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt

def get(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(" ", strip=True).lower()

        keywords = ["2 hour delay", "2-hour delay", "closed", "canceled", "cancelled" , "no school", "snow day"]

        for word in keywords:
            if word in text:
                return word
        return "n"
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return "n"

districts = {
    "FCPS": "https://www.fcps.edu/",
    "LCP": "https://www.lcps.org/",
    "Arlington County": "https://www.apsva.us/"
}

while True:
    for district, url in districts.items():
        status = get(url)
        print(f"{district} status: {status}")

        if status != "n":
            plt.plot([1, 2, 3], [1, 2, 3])
            plt.title(f"{district} Status Alert: {status}")
            plt.show()
    time.sleep(600)
