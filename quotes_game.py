import requests
import random
import csv
from bs4 import BeautifulSoup

csv_file = open("quotes.csv", "r", encoding = "utf-8")
quotes = []
authors = []
bios = []

for quote, author, bio in csv.reader(csv_file, delimiter=","):
    quotes.append(quote)
    authors.append(author)
    bios.append(bio)

play_again = "y"
while play_again == "y" or play_again == "yes": 
    answer = random.randint(0, len(quotes))
    print(quotes[answer])
    guesses_remaining = 4
    while guesses_remaining != 0: 
        guess = input("Who said or wrote this? ").lower()
        if guess == authors[answer].lower(): 
            print("Congrats! You win!")
            break
        else: 
            guesses_remaining -= 1
            if guesses_remaining == 3: 
                first_initial = authors[answer][0]
                print(f"Nope! Here's a hint: The first name begins with {first_initial}.")
            elif guesses_remaining == 2: 
                reverse = authors[answer][::-1]
                space = reverse.find(' ')
                last_initial = reverse[space-1]
                print(f"Sorry! Here's another hint: The last name begins with {last_initial}.")
            elif guesses_remaining == 1: 
                hint_url = "http://quotes.toscrape.com" + bios[answer]
                hint_response = requests.get(hint_url)
                hint_soup = BeautifulSoup(hint_response.text, "html.parser")
                birthday = hint_soup.find(class_ = "author-born-date").get_text()
                born_in = hint_soup.find(class_ = "author-born-location").get_text()
                print(f"This author was born on {birthday} in {born_in}.")
            else: 
                print(f"Oof! The correct answer was {authors[answer]}.")
            print(f"You have {guesses_remaining} guesses remaining.")
    play_again = input("Would you like to play again? (y/n) ").lower()
