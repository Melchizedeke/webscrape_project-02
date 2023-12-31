#Essential libraries import
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice


first_url = "https://quotes.toscrape.com"
user_name = input('Welcome to the John Igoche guessing game, please enter you username : ')

def scrape_quotes():
    quotes_list = []
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
            # sleep(3)
    return quotes_list
    
def game_on(quotes):
    quote = choice(quotes)
    guesses_left = 4

    print(quote["text"])
    print(quote["author"])
    guess = ""
    while guess.lower() != quote["author"].lower() and guesses_left > 0:
        guess = input(f"This quotes was made by who? Guesses remaining: {guesses_left} \n")
        guesses_left -= 1
        if guess.lower() == quote["author"].lower():
            print(f"Hello {user_name} you got it right!")
            break
        if guesses_left == 3:
            res = requests.get(f"{first_url}{quote['author-bio']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").getText()
            birth_place = soup.find(class_="author-born-location").getText()
            print(f"Hint: The author was born on {birth_date} {birth_place}")
        elif guesses_left == 2:
            print(f"Hint : The author's name begins with {quote['author'][0]}")
        elif guesses_left == 1:
            last_initial = quote["author"].split(' ')[1][0]
            print(f"Hint : The author's last name starts with {last_initial}")
        else:
            print(f'You ran out of guess. The right answer is {quote["author"]}')
            print(f"")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")
        if again.lower() in ('yes','y'):
            print(f'Okay {user_name}, lets go again.')
            return game_on(quotes)
        elif again.lower() in ('no','n'): 
            print(f"Okay {user_name}, goodbye!")
        else:
            print(f"Hello, {user_name}, please select a valid option.")

quotes = scrape_quotes()
game_on(quotes)