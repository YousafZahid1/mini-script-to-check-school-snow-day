import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt

def get(url):
    
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ", strip=True).lower()

    keywords = ["2 hour delay", "2-hour delay", "closed", "canceled", "cancelled", "no school", "snow day", "two-hour delay", "two hours late","two hours"]

    for word in keywords:
        if word in text:
            return word
    return "n"


url = "https://www.fcps.edu/alert_msg_feed"
while True:
    status = get(url)
    print("FCPS status:", status)

    if status != "n":
        plt.plot([1, 2, 3], [1, 2, 3])
        plt.title(f"FCPS Status Alert: {status}")
        plt.show()
        break 
    time.sleep(600)
