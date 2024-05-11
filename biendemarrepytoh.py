"""for i in range(10):
    if i == 5:
        break
    print(i)"""
import requests
from bs4 import BeautifulSoup

url="https://www.gov.uk/"
page= requests.get(url)
reponse = BeautifulSoup(page.content,"htlm.parse")
