import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt


DISTRICTS = {
    "FCPS": "https://www.fcps.edu/",
    "LCPS": "https://www.lcps.org/",
    "APS": "https://www.apsva.us/",
}


def get(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ", strip=True).lower()

    keywords = ["2 hour delay", "2-hour delay", "closed", "canceled", "cancelled" , "no school", "snow day"]

    for word in keywords:
        if word in text:
            return word
    return "n"


while True:
    alerts = {}
    for name, url in DISTRICTS.items():
        try:
            status = get(url)
        except requests.RequestException as e:
            status = f"error: {e}"
        print(f"{name} status: {status}")
        if status != "n":
            alerts[name] = status

    if alerts:
        labels = list(alerts.keys())
        fig, ax = plt.subplots()
        ax.barh(labels, [1] * len(labels), color="red")
        ax.set_xlabel("Alert")
        title = ", ".join(f"{k}: {v}" for k, v in alerts.items())
        ax.set_title(f"Snow Day Alert: {title}")
        plt.tight_layout()
        plt.show()
        break

    time.sleep(600)
