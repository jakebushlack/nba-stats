from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player
import csv
from BR_Scraper_0_8 import scrape
from BR_Scraper_0_8 import get_players

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
    temp = []
    for player in get_players(file_name):
        temp.append(player)
    if players:
        for player in players:
            for x in temp:
                for attr in x.__dict__.keys():
                    if player.player == x.player:
                        # print(attr)
                        player.__setattr__(attr, x.__dict__[attr])
                    else:
                        continue

    else:
        for player in temp:
            players.append(player)

# print("Stats:\n")
# for each in players[0].__dict__.keys():
#     print(each)
# for player in players:
#     print("%s | %d | %.2f | %.2f" % (player.player, int(player.age), float(player.trb_per_g), float(player.ast_per_g)))
