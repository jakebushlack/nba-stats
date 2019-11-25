from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player
import csv
from BR_Scraper_0_7 import scrape
from BR_Scraper_0_7 import get_players

totals_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
game_url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'
minute_url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_minute.html'
poss_url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_poss.html'
advanced_url = 'https://www.basketball-reference.com/leagues/NBA_2020_advanced.html'
urls = [totals_url, game_url, minute_url, poss_url, advanced_url]
players = []

#test
file_names = []
for url in urls:
    file_name = url[54:-5]
    file_names.append(file_name)
    # print("Processing %s..." %(file_name))
    # scrape(url)
for file_name in file_names:
    for player in get_players(file_name):
        players.append(player)

print(len(players))

