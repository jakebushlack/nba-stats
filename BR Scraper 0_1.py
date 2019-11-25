from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player

szn_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
game_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
poss_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
min_url = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
adv_url = 'https://www.basketball-referx4ence.com/leagues/NBA_2020_totals.html'

uClient = uReq(szn_url)
html = uClient.read()
uClient.close()

page_soup = soup(html, "html.parser")
tables = page_soup.findAll("tr", {"class": "full_table"})
list_of_players = []


for player in tables:
    name = str(player.find("td", {"data-stat": "player"}).text)
    position = str(player.find("td", {"data-stat": "pos"}).text)
    age = int(player.find("td", {"data-stat": "age"}).text)
    team = str(player.find("td", {"data-stat": "team_id"}).text)
    games_played = int(player.find("td", {"data-stat": "g"}).text)
    games_started = int(player.find("td", {"data-stat": "gs"}).text)
    minutes_played = int(player.find("td", {"data-stat": "mp"}).text)
    fg_made = int(player.find("td", {"data-stat": "fg"}).text)
    fg_att = int(player.find("td", {"data-stat": "fga"}).text)
    three_point_made = int(player.find("td", {"data-stat": "fg3"}).text)
    three_point_attempts = int(player.find("td", {"data-stat": "fg3a"}).text)
    two_point_made = int(player.find("td", {"data-stat": "fg2"}).text)
    two_point_attempts = int(player.find("td", {"data-stat": "fg2a"}).text)
    free_throws_made = int(player.find("td", {"data-stat": "ft"}).text)
    free_throws_attempted = int(player.find("td", {"data-stat": "fta"}).text)
    defensive_rebounds = int(player.find("td", {"data-stat": "drb"}).text)
    offensive_rebounds = int(player.find("td", {"data-stat": "orb"}).text)
    assists = int(player.find("td", {"data-stat": "ast"}).text)
    steals = int(player.find("td", {"data-stat": "stl"}).text)
    blocks = int(player.find("td", {"data-stat": "blk"}).text)
    turnovers = int(player.find("td", {"data-stat": "tov"}).text)
    personal_fouls = int(player.find("td", {"data-stat": "pf"}).text)
    list_of_players.append(Player(name, position, age, team, games_played, games_started, minutes_played, fg_made,
                                  fg_att, three_point_made, three_point_attempts, two_point_made, two_point_attempts,
                                  free_throws_made, free_throws_attempted, offensive_rebounds, defensive_rebounds,
                                  assists, steals, blocks, turnovers, personal_fouls))

scoring_leaders = sorted(list_of_players, key=lambda x: x.ptspg, reverse=True)
assists_leaders = sorted(list_of_players, key=lambda x: x.astpg, reverse=True)
rebounding_leaders = sorted(list_of_players, key=lambda x: x.t_rebpg, reverse=True)

scoring_20 = []
assisting_20 = []
rebounding_20 = []

i = 0
while i < 20:

    scoring_20.append(scoring_leaders[i].name)
    assisting_20.append(assists_leaders[i].name)
    rebounding_20.append(rebounding_leaders[i].name)

    i+=1

for players in scoring_20:
    if assisting_20.__contains__(players) and rebounding_20.__contains__(players):
        print(players)

