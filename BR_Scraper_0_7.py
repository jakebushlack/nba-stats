from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player
import csv
import io


def scrape(url):
    file_name = url[54:-5]
    table_name = file_name + "_stats"
    players = []
    uClient = uReq(url)
    html = uClient.read()  # STORE HTML DATA FROM WEBPAGE TO A VARIABLE
    uClient.close()
    page_soup = soup(html, "html.parser")
    html_table = page_soup.find('table', {'id': table_name})

    with open(file_name, 'w', encoding="utf-8") as file_contents:
        for stat in html_table.thead.find_all("th"):
            if stat.get('data-stat') == 'ranker':
                pass
            else:
                file_contents.write(str(stat.get('data-stat') + ','))
        for row in page_soup.find_all('tr', {"class": "full_table"}):
            file_contents.write('\n')
            # print(row)
            for stat in row.find_all("td"):
                file_contents.write(str(stat.text) + ',')
    return file_name


def get_players(file_name):
    categories = []
    players = []
    try:
        with open(file_name, 'r', encoding="utf-8") as file_contents:
            csv_reader = csv.reader(file_contents, delimiter=',')
            row_count = 0
            for row in csv_reader:
                player = Player()
                if row_count == 0:
                    for col in row:
                        if col:
                            categories.append(col)
                    row_count += 1
                else:
                    cat_count = 0
                    for col in row:
                        if col:
                            try:
                                print(categories.index(col)).__setattr__(categories.index(col), col)
                            except IndexError:
                                print("Error")
                            cat_count += 1
                    players.append(player)
        print(player.__dict__.keys())
    except OSError:
        print(OSError)
    return players

