from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'

uClient = uReq(my_url)
html = uClient.read()
uClient.close()

page_soup = soup(html, "html.parser")
tables = page_soup.findAll("tr", {"class": "full_table"})

print(len(tables))
print(type(tables[2]))
print(tables[2])

print(tables[2].find("td", {"data-stat": "age"}).text)

