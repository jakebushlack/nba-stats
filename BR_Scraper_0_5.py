from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player
import csv
import io


def scrape(url):
    file_name = url[54:-5]
    table_name = url[54:-5] + "_stats"
    players = []
    uClient = uReq(url)
    html = uClient.read()  # STORE HTML DATA FROM WEBPAGE TO A VARIABLE
    uClient.close()
    with open(file_name, "w") as f:
        f.write(str(html))
    return file_name


def get_players(file_name):
    categories = []
    players = []
    try:
        with open(file_name, 'r') as file_contents:
            table_name = file_name + "_stats"
            page_soup = soup(file_contents, "html.parser")
            html_table = page_soup.find('table', {'id': table_name})
            for x in html_table.thead.find_all("th"):
                stat_cats = x.get("data-stat")
            for row in page_soup.find_all('tr', {"class": "full_table"}):
                player = Player()
                for stat in row.find_all("td"):
                    setattr(player, stat.get('data-stat'), stat.text)
                players.append(player)

    except OSError:
        print(OSError)
    return players


players = get_players(scrape('https://www.basketball-reference.com/leagues/NBA_2020_totals.html'))

for player in players:
    print(player.player)