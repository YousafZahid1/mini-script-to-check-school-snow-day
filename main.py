import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import random

def get(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ", strip=True).lower()

    delay_keywords = [
        "2 hour delay",
        "2-hour delay",
        "two-hour delay",
        "two hours late",
        "two hours"
    ]

    closed_keywords = [
        "schools closed",
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
