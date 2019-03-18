import requests, time

from bs4 import BeautifulSoup



txtFile = open("top 50 IMDB.txt", "a", encoding = "utf-8")


movieNamez = list()
movieDates = list()
movieNumbers = list()
movieVotes = list()
moviePrice = list()

key = 1

old = 0
new = 1

url = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating,desc&start=0&ref_=adv_nxt"

while key < 6:

    url = url.replace("start=" + str(old), "start=" + str(new))   
    response = requests.get(url)

    content = response.content

    soup = BeautifulSoup(content, "html.parser")
     
    
    for header in soup.find_all("h3", {"class": "lister-item-header"}):
        for names in header.find_all("a"):
            movieNamez.append(names.text)
        for numbers in header.find_all("span", {"class": "lister-item-index unbold text-primary"}):
            movieNumbers.append(numbers.text)
        for dates in header.find_all("span", {"class": "lister-item-year text-muted unbold"}):
            movieDates.append(dates.text)

    for votes in soup.find_all("p", {"class": "sort-num_votes-visible"}):
        for x in votes.find_all("span", {"name": "nv"}):
            if "$" not in x.text:
                movieVotes.append(x.text)
            
    old = new
    new += 50
    key += 1

ooo = 0

for f in zip(movieNumbers, movieNamez, movieDates, movieVotes):
    print(*f, "votes")