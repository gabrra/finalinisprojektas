# scraper_h3.py
from bs4 import BeautifulSoup
import requests
from typing import List


def fetch_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_html(html: str, class_name: str) -> List[str]:
    soup = BeautifulSoup(html, 'html.parser')
    # for lrt change div to h3
    blocks = soup.find_all('h3', class_=class_name)
    titles = [block.get_text(strip=True) for block in blocks]
    return titles


def get_sorted_titles(url: str, class_name: str) -> List[str]:
    html = fetch_html(url)
    titles = parse_html(html, class_name)
    return sorted(titles)
