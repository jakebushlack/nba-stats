from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player

szn_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
game_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
poss_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
min_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
adv_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'

stats = {"ast", "pts", "stl", "blk", "g", "trb"}
list_of_players = []


def scraper(url):
    uClient = uReq(url)
    html = uClient.read()
    uClient.close()
    page_soup = soup(html, "html.parser")
    tables = page_soup.findAll("tr", {"class": "full_table"})
    return tables


def get_stat(_table, _stat):
    try:
        stat = int(_table.find("td", {"data-stat": _stat}).text)
        setattr(player, _stat, stat)
    except ValueError:
        stat = str(_table.find("td", {"data-stat": _stat}).text)
        setattr(player, _stat, stat)


for table in scraper(szn_url):
    player = Player()
    setattr(player, "name", str(table.find("td", {"data-stat": "player"}).text))
    for each_stat in stats:
        get_stat(table, each_stat)
    setattr(player, "ppg", player.pts/player.g)
    setattr(player, "rpg", player.trb / player.g)
    setattr(player, "apg", player.ast / player.g)
    list_of_players.append(player)

#
scoring_leaders = sorted(list_of_players, key=lambda x: x.ppg, reverse=True)

for leader in scoring_leaders:
    print(leader.name + ' | %.2f' % (leader.ppg))
# assists_leaders = sorted(list_of_players, key=lambda x: x.apg, reverse=True)
# rebounding_leaders = sorted(list_of_players, key=lambda x: x.rpg, reverse=True)
# scoring_50 = []
# assisting_50 = []
# rebounding_50 = []
#
# i = 0
#
# while i < 50:
#     scoring_50.append(scoring_leaders[i])
#     assisting_50.append(assists_leaders[i])
#     rebounding_50.append(rebounding_leaders[i])
#     i += 1
#
#
# print("NBA top-50 in PPG, RPG, and APG")
# for players in scoring_50:
#     if assisting_50.__contains__(players) and rebounding_50.__contains__(players):
#         print("%s | PPG: %.1f | RPG: %.1f | APG: %.1f" % (players.name, players.ppg, players.rpg, players.apg))
