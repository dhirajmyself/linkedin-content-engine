import requests
from bs4 import BeautifulSoup

def extract_author(url):
    r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"},timeout=20)
    soup=BeautifulSoup(r.text,"html.parser")
    return soup.title.text if soup.title else ""