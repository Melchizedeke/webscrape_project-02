#Essential libraries import
import requests
from bs4 import BeautifulSoup
from time import sleep

quotes_list = []
first_url = "https://quotes.toscrape.com"
url = "/page/1"


while url:
    res = requests.get(f"{first_url}{url}")
    print(f"Currently scrapping {first_url}{url}")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    # Looping through the quotes
    for quote in quotes:
        quotes_list.append({
            "text":quote.find(class_="text").getText(),
            "author":quote.find(class_="author").getText(),
            "author-bio":quote.find("a")["href"]
        })
    #Moving to the next page
    next_page = soup.find(class_="next")
    url = next_page.find("a")["href"] if next_page else None
    sleep(3)

# print(next_page.find("a")["href"])

print(quotes_list)