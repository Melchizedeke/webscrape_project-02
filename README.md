# webscrape_project-02

A webscraping game project to scrape the website : https://quotes.toscrape.com/ to get quotes from selected famous authors using "bs4 - BeautifulSoup" and "requests".

The goal of this project is to loop through all of the pages of the website, and for each given quote, grab the the quote itself, the name of the author as well as the href of the link to the author's bio and store them in a list object.

Next, we display the quotes to the users and ask them to guess the author correctly within a space of four(4) possible guesses. For every incorrect guesses, the number of possible guesses decrement until the user runs out of guesses where the game ends. But if the user gets the guess correctly, the user has an opportunity to either play again or not.

After every incorrect guess, the player gets a hint as to what the correct answer is and when the guesses are exhausted, the application automatically tells the user the answer.

# sleep(3)

The three seconds delay from the time module was necessary to ensure that there is a delay of three between successive pages in order to scrape ethically and not over burden the websites server thereby slowing access to it and its user experience for other users visiting it. It is the morally right thing to do when scraping through multiple pages of a website.
