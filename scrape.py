import requests
from bs4 import BeautifulSoup
from csv import writer

url = "http://quotes.toscrape.com"
quotes = []
authors = []
bios = []

while True: 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quote_block = soup.find_all(class_="quote")

    for q in quote_block: 
        quotes.append(q.find(class_ = "text").get_text())
        authors.append(q.find(class_ = "author").get_text())
        bios.append(q.find("a")["href"])

    next_button = soup.find(class_ = "next")
    if next_button: 
        page = next_button.find("a")["href"]
        url = "http://quotes.toscrape.com" + page
    else: 
        break

with open("quotes.csv", "w", encoding = "utf-8", newline='') as file: 
    csv_writer = writer(file)
    rcount = 0 
    for row in quotes: 
        csv_writer.writerow([quotes[rcount], authors[rcount], bios[rcount]])
        rcount += 1
