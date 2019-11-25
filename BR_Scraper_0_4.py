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
    page_soup = soup(html, "html.parser")
    html_table = page_soup.find('table', {'id': table_name})
    headers = [th.text.encode("utf-8") for th in page_soup.select("tr th")]  # FIND HEADERS AND ENCODE
    # head = html_table.find("thead")
    stat_cats = [x.get("data-stat") for x in html_table.thead.find_all("th")]
    with open(file_name, "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        print()
        # FIND DATA AND ENCODE
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")]for row in page_soup.select("tr + tr")])
    return stat_cats


def pull(url, stat_cats):
    file_name = url[54:-5]
    categories = []
    players = []
    try:
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                player = Player()
                if len(line) > 29:
                    del line[29:]
                    print(line)
                    # setattr(player, line, '')
                if line:
                    for stats in line:
                        stats = stats[2:-1]
                        setattr(player, stats, stats)
                        players.append(player)
                        print(player.player)
                        # print(line)
    except OSError:
        print(OSError)
