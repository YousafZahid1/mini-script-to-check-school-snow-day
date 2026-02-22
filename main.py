import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import random

def get(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "xml")
    text = soup.get_text(" ", strip=True).lower()
    text = (text.replace("\u2010", "-")
                .replace("\u2011", "-")
                .replace("\u2012", "-")
                .replace("\u2013", "-")
                .replace("\u2014", "-"))

    delay_keywords = [
        "2 hour delay",
        "2-hour delay",
        "two-hour delay",
        "two hours late",
        "open two hours late"
    ]

    closed_keywords = [
        "schools closed",
        "school closed",
        "closed",
        "no school",
        "snow day"
    ]

    for word in closed_keywords:
        if word in text:
            return "CLOSED"

    for word in delay_keywords:
        if word in text:
            return "DELAY"

    return None


url = "https://www.fcps.edu/alert_msg_feed"

while True:
    status = get(url)
    print("FCPS status:", status)

    if status == "DELAY":
        x = [random.random() for _ in range(20)]
        y = [random.random() for _ in range(20)]
        plt.scatter(x, y, c='yellow')
        plt.title("FCPS: 2 Hour Delay")
        plt.show()
        break

    elif status == "CLOSED":
        x = [random.random() for _ in range(20)]
        y = [random.random() for _ in range(20)]
        plt.scatter(x, y, c='red')
        plt.title("FCPS: SCHOOL CLOSED")
        plt.show()
        break

    time.sleep(600)
