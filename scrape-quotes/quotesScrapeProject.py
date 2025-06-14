from bs4 import BeautifulSoup
import requests
import time
from random import choice

# Using `bs4` and `requests` to get the data
base_url = "https://quotes.toscrape.com/"
url = "/page/1"
all_quotes = []

# Data Collection from the quotes site
while url:
    response = requests.get(f"{base_url}{url}")
    print(f"Now scraping: {url}")
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    quote_list = soup.select(".quote")
    # run a loop and store the contents in the dictionary
    for quote in quote_list:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio": quote.find('a').get("href")
        })
    time.sleep(0.1) #delay the pings
    # Continue to scrape to the next page until theres no Next button available
    next_btn = soup.find(class_="next")
    url = next_btn.find("a").get("href") if next_btn else None
# print(all_quotes)

# Game Logic
quote = choice(all_quotes)
remaining_guesses = 4
print(quote["text"])
# print(quote["author"])
guess = ''
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(f"Who said this quote? Remaining guesses: {remaining_guesses} \n")
    if guess.lower() == quote["author"].lower():
        print("You guessed it right")
        break
    remaining_guesses -= 1
    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio']}")
        soup = BeautifulSoup(res.text, "html.parser")
        author_born_date = soup.find(class_="author-born-date").get_text()
        author_born_location = soup.find(class_="author-born-location").get_text()
        print(f"Incorrect, here's a hint. This author was born on {author_born_date}, {author_born_location} ")
    elif remaining_guesses == 2:
        author_first_initial = quote["author"][0]
        print(f"Author's first initial:", author_first_initial)
    elif remaining_guesses == 1:
        author_last_initial = quote["author"].split(" ")[1][0]
        print(f"Author's last initial:", author_last_initial)
    else:
        print(f"You ran out of guesses. Author's name is {quote['author']}")
        break


